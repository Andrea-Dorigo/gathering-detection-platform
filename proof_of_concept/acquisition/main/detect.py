import urllib.request
import requests
from urllib.request import urlopen, Request
import os
import time
import string
import glob
import sys
import json
import subprocess
from datetime import datetime,timedelta
from mongoengine import *
import logging
import cv2

from weather import get_current_weather
from get_frames import get_frames, extract_frame_from_video_url
from cut_frame import cut_frames, cut_frame_in_six
from yolo import detect

from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8')
                         )


logging.basicConfig(filename='test.log', level=logging.DEBUG)

statement = True
PATH_WEBCAM_JSON = "../webcams.json"
PATH_M3U8 = "../m3u8/"
PATH_VIDEOS = "../videos/"
PATH_FRAMES = "../frames/"
PATH_FRAMES_PIECES= "../frames_pieces/"

DETECTIONS_INTERVAL = 300



def fetch_read_m3u8(webcam_link, webcam_prefix):
        try:
            response = requests.get(webcam_link)
            # scorri le righe del m3u8 fino al primo video .ts e salvalo in video_link
            for line in response.text.splitlines():
                if line.endswith('.ts'):
                    return webcam_prefix + line

        except:
            logging.info('Eccezione fetch_read_m3u8 ore: ' + str(datetime.now()) )
            logging.error(sys.exc_info())


def main():
    while True :

        # imposta il tempo di attesa fra un conteggio di persone e l'altro
        print("Orario di inizio detection: " + str(datetime.now()) )
        t_end = datetime.now().replace(microsecond=0) + timedelta(seconds=DETECTIONS_INTERVAL)
        print("Orario di fine detection:   " + str(t_end) )

        # leggi il file json contenente i dati delle webcam
        with open(PATH_WEBCAM_JSON) as f:
          json_data = json.load(f)

        # scorri fra tutte le webcams presenti nel file json
        for webcam in json_data["webcams"]:
            print("Raccolta dati per: " + webcam["location"] + ", " + webcam["city"])
            # ottieni la temperatura e il meteo al tempo dell'acquisizione;
            try:
                temperature, weather_description = get_current_weather(webcam["latitude"], webcam["longitude"])
            except:
                print('Exception nel weather')
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue

            #imposta l'orario e la data di acquisizione
            current_time = current_date = datetime.now()

            try:
                video_link = fetch_read_m3u8(webcam["link"], webcam["url_prefix"])
            except:
                print("Failed to fetch/read m3u8")
                # continue

                # scarica il video dal link appena ricavato

            try:
                #urllib.request.urlretrieve(video_link, PATH_VIDEOS+"Video" + ".ts")
                frame_is_read, frame = extract_frame_from_video_url(video_link)
                print(frame_is_read)
            except:
                print('Exception: video non disponibile: ' + webcam["location"])
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue

            try:
                frame_part = cut_frame_in_six(frame)

            except:
                print('Exception')
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue

            persone_contate = 0

            # conta le persone in ogni sottoframe
            for frame in frame_part:
                persone_contate = persone_contate + detect(frame)

            print("Persone: " + str(persone_contate))
            
            data = { 'id_webcam': webcam["id_webcam"], 
            		'city': webcam["city"], 
            		'location': webcam["location"],
            		'latitude': webcam["latitude"],
            		'longitude': webcam["longitude"], 
            		'numPeople': persone_contate, 
            		'date': current_date.strftime('%Y-%m-%d %H:%M:%S.%f'), 
            		'time': current_time.strftime('%Y-%m-%d %H:%M:%S.%f'), 
            		'type': 0, 
            		'weather_description': weather_description, 
            		'temperature': temperature, 
            		'day_of_week': datetime.now().date().weekday()}
            producer.send('gdp', value=data)
            print("ho fatto kafka")
                # inserisci i risultati nel db


        print("waiting for: " + str((t_end - datetime.now()).total_seconds()))
        time.sleep((t_end - datetime.now()).total_seconds())

main()

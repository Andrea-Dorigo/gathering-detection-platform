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
import numpy as np

from weather import get_current_weather
from get_frames import  extract_frame_from_video_url
from cut_frame import cut_frame_in_six
from yolo import count_objects_in_frame

from json import dumps


logging.basicConfig(filename='test.log', level=logging.DEBUG)

statement = True
PATH_WEBCAM_JSON = "../../../webcams.json"

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
                print('Condizioni meteo ottenute con successo')
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
                frame_is_read, frame = extract_frame_from_video_url(video_link)
                cv2.imwrite('frame' + str(webcam["city"]) + '.jpg', frame)
                print('Frame estratto con successo')
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

            persone_contate = count_objects_in_frame(frame_part)

            print("Persone: " + str(persone_contate))

            #unisco i frame con i riquadri

            img1 = cv2.imread("detection0.jpg")
            img2 = cv2.imread("detection1.jpg")
            img3 = cv2.imread("detection2.jpg")
            img4 = cv2.imread("detection3.jpg")
            img5 = cv2.imread("detection4.jpg")
            img6 = cv2.imread("detection5.jpg")
            col1 = np.concatenate((img1, img2), axis=0)
            col2 = np.concatenate((img3, img4), axis=0)
            col3 = np.concatenate((img5, img6), axis=0)
            col12 = np.concatenate((col1, col2), axis=1)
            col123 = np.concatenate((col12, col3), axis=1)
            cv2.imwrite('complete' + str(webcam["city"])+'.jpg', col123)



main()

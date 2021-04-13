#start with python3 get_video.py
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

from weather import get_current_weather
from get_frames import get_frames
from cut_frame import cut_frames

connect("GDP-test", host = "localhost", port = 27017)
logging.basicConfig(filename='test.log', level=logging.DEBUG)

statement = True
PATH_WEBCAM_JSON = "../webcams.json"
PATH_M3U8 = "../m3u8/"
PATH_VIDEOS = "../videos/"
PATH_FRAMES = "../frames/"
PATH_FRAMES_PIECES= "../frames_pieces/"
# path_video = "../m3u8/"

# TODO: aggiungere le costanti che indicano i path (come quella qui sopra)

DETECTIONS_INTERVAL = 300

class Detection(Document):
    id_webcam = IntField(required=True)
    city = StringField(required=True)
    location = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    numPeople = IntField(required=True)
    date = DateTimeField(required=True)
    time = DateTimeField(required=True)
    type = IntField(required=True)
    weather_description = StringField()
    temperature = FloatField()
    day_of_week = IntField()


def fetch_read_m3u8(webcam):
        try:
            response = requests.get(webcam["link"])
            # scorri le righe del m3u8 fino al primo video .ts e salvalo in video_link
            for line in response.text.splitlines():
                if line.endswith('.ts'):
                    return webcam["url_prefix"] + line

        except:
            logging.info('Eccezione fetch_read_m3u8 ore: ' + str(datetime.now()) )
            logging.error(sys.exc_info())


def main():
    # A fini di testing, viene fatta una sola detection (loops < 1);
    # sostituisci "while loops < 1:" con "while True:" per l'esecuzione continua
    #loops = 0
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
                video_link = fetch_read_m3u8(webcam)
            except:
                print("Failed to fetch/read m3u8")
                continue

                # scarica il video dal link appena ricavato
            try:
                urllib.request.urlretrieve(video_link, PATH_VIDEOS+"Video" + ".ts")
            except:
                print('Exception: video non disponibile: ' + webcam["location"])
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue

                # estrai un frame dal video
                #exec(open('get_frames.py').read())
            try:
                get_frames(PATH_VIDEOS, PATH_FRAMES)
                if get_frames(PATH_VIDEOS, PATH_FRAMES):
                    print("Acquisizione Frame completata")
            except:
                print('Exception')
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue
                # dividi il frame in 6 per un migliore affidabilita' nel riconoscimento
                #exec(open('cut_frame.py').read())
            try:
                cut_frames(PATH_FRAMES, PATH_FRAMES_PIECES)
                if cut_frames(PATH_FRAMES, PATH_FRAMES_PIECES):
                    print("Taglio dei frame in foto completata")

            except:
                print('Exception')
                logging.info('Eccezione ore: ' + str(datetime.now()) )
                logging.error(sys.exc_info())
                continue

            # conta le persone in ogni sottoframe
            persone_contate = 0
            for file in glob.glob(PATH_FRAMES_PIECES + "*.png"):
                result = subprocess.run(['python3' , 'yolo.py' , '--image' , PATH_FRAMES_PIECES + file], capture_output=True)
                persone_contate += result.stdout.decode().count('person')
                print("Persone contate fino ad ora: " + str(persone_contate))

            print("Ci sono " + str(persone_contate) + " in totale")
                # inserisci i risultati nel db
            detection = Detection(
                id_webcam = webcam["id_webcam"],
                city = webcam["city"],
                location = webcam["location"],
                latitude = webcam["latitude"],
                longitude = webcam["longitude"],
                numPeople = persone_contate,
                date = current_date,
                time = current_time,
                type = 0,
                weather_description = weather_description,
                temperature = temperature,
                day_of_week =  datetime.now().date().weekday()
                ).save()
                #time.sleep((t_end - datetime.now()).total_seconds())

        #loops = loops + 1
        print("waiting")
        print((t_end - datetime.now()).total_seconds())
        time.sleep((t_end - datetime.now()).total_seconds())

main()

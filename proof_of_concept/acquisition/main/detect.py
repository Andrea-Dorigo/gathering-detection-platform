#start with python3 get_video.py
import urllib.request
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

INTERVAL_BETWEEN_DETECTIONS = 300

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

# leggi il file json contenente i dati delle webcam
with open(PATH_WEBCAM_JSON) as f:
  json_data = json.load(f)


# A fini di testing, viene fatta una sola detection (loops < 1);
# sostituisci "while loops < 1:" con "while True:" per l'esecuzione continua
#loops = 0
while True :

    # imposta il tempo di attesa fra un conteggio di persone e l'altro
    t_start = datetime.now().replace(microsecond=0)
    print(datetime.now())
    t_end = t_start + timedelta(seconds=INTERVAL_BETWEEN_DETECTIONS)
    print(t_start)
    print(t_end)
    # scorri fra tutte le webcams presenti nel file json
    for webcam in json_data["webcams"]:

        # ottieni la temperatura e il meteo al tempo dell'acquisizione;
        try:
            [temperature, weather_description] = get_current_weather(webcam["latitude"], webcam["longitude"])
        except:
            print('Exception')
            logging.info('Eccezione ore: ' + str(datetime.now()) )
            logging.error(sys.exc_info())
            continue

        #imposta l'orario e la data di acquisizione
        current_time = datetime.now()
        current_date = datetime.now()

            # scarica il file m3u8 contenente i link ai video
        m3u8_file_path = PATH_M3U8 + webcam["location"] + ".m3u8"
        try:
            urllib.request.urlretrieve(webcam["link"], m3u8_file_path )
        except:
            print('Exception')
            logging.info('Eccezione ore: ' + str(datetime.now()) )
            logging.error(sys.exc_info())
            continue

            # scorri le righe del file m3u8 fino a che non trovi un link al video .ts e salvalo in video_link
            # si ferma al primo link perche' ci basta meno di un video al minuto
        for line in open(m3u8_file_path, "r").readlines():
            if line[:-1].endswith('.ts'):
                video_link = line[:-1]
                if not line[:-1].startswith('https'):
                    video_link = webcam["url_prefix"] + line[:-1]
                print(video_link)
                break

            # scarica il video dal link appena ricavato
        try:
            urllib.request.urlretrieve(video_link, PATH_VIDEOS+"Video" + ".ts")
        except:
            print('Exception')
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
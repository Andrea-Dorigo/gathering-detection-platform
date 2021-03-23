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

from weather import get_current_weather
from get_frames import get_frames
from cut_frame import cut_frames

connect("GDP-test", host="localhost", port=27017)

statement = True
path_frame1 = "../frames_pieces/*.png"
# path_video = "../m3u8/"

# TODO: aggiungere le costanti che indicano i path (come quella qui sopra)

INTERVAL_BETWEEN_DETECTIONS = 20

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
with open('../webcams.json') as f:
  json_data = json.load(f)


# A fini di testing, viene fatta una sola detection (loops < 1);
# sostituisci "while loops < 1:" con "while True:" per l'esecuzione continua
loops = 0
while loops < 1 :

    # imposta il tempo di attesa fra un conteggio di persone e l'altro
    t_end = datetime.now() + timedelta(seconds=INTERVAL_BETWEEN_DETECTIONS)

    # scorri fra tutte le webcams presenti nel file json
    for webcam in json_data["webcams"]:

        # ottieni la temperatura e il meteo al tempo dell'acquisizione;
        [temperature, weather_description] = get_current_weather(webcam["latitude"], webcam["longitude"])

        #imposta l'orario e la data di acquisizione
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().date()

        try:

            # scarica il file m3u8 contenente i link ai video
            m3u8_file_path = "../m3u8/" + webcam["location"] + ".m3u8"
            urllib.request.urlretrieve(webcam["link"], m3u8_file_path )

            # scorri le righe del file m3u8 fino a che non trovi un link al video .ts e salvalo in video_link
            # si ferma al primo link perche' ci basta meno di un video al minuto
            for line in open(m3u8_file_path, "r").readlines():
                if line[:-1].endswith('.ts'):
                    video_link = line[:-1]
                    if not line[:-1].startswith('https'):
                        video_link = 'https://cdn-002.whatsupcams.com/hls/' + line[:-1]
                    print(video_link)
                    break

            # scarica il video dal link appena ricavato
            urllib.request.urlretrieve(video_link, "../videos/Video" + webcam["location"] + ".ts")

            # estrai un frame dal video
            #exec(open('get_frames.py').read())
            get_frames(statement)
            if statement is True:
                print("Acquisizione Frame completata")
            # dividi il frame in 6 per un migliore affidabilita' nel riconoscimento
            #exec(open('cut_frame.py').read())
            cut_frames(statement)
            if statement is True:
                print("Taglio dei frame in foto completata")

            # conta le persone in ogni sottoframe
            persone_contate = 0
            for file in glob.glob(path_frame1):
                result = subprocess.run(['python3','yolo.py','--image','../frames_pieces/'+file], capture_output=True)
                persone_contate += result.stdout.decode().count('person')
                print("Persone contate fino ad ora: "+str(persone_contate))

            print("Ci sono "+str(persone_contate) + " in totale")

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
        except:
            time.sleep((t_end - datetime.now()).total_seconds())

    loops = loops + 1

    #time.sleep((t_end - datetime.now()).total_seconds())

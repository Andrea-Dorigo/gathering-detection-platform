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

from get_current_weather import get_current_weather

connect("GDP-test", host="localhost", port=27017)

path_frame1 = "../frames_pieces/*.png"
# path_video = "../m3u8/"

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

with open('../webcams.json') as f:
  json_data = json.load(f)

i = 0
while i < 1 :
    t_end = datetime.now() + timedelta(seconds=INTERVAL_BETWEEN_DETECTIONS)
    for webcam in json_data["webcams"]:
        [temperature, weather_description] = get_current_weather(webcam["latitude"], webcam["longitude"])
        orario = datetime.now().strftime("%H:%M:%S")
        data_dato = datetime.now().date()

        try:
            m3u8_file_path = "../m3u8/"+webcam["location"]+".m3u8"
            urllib.request.urlretrieve(webcam["link"], m3u8_file_path )

            for line in open(m3u8_file_path, "r").readlines():
                if line[:-1].endswith('.ts'):
                    video_link = line[:-1]
                    if not line[:-1].startswith('https'):
                        video_link = 'https://cdn-002.whatsupcams.com/hls/' + line[:-1]
                    print(video_link)
                    break

            urllib.request.urlretrieve(video_link, "../videos/Video" + webcam["location"] + ".ts")

            exec(open('get_frames.py').read())
            exec(open('cut_frame.py').read())

            persone_contate = 0
            # print("after cut_frame")

            for file in glob.glob(path_frame1):

                result = subprocess.run(['python3','yolo.py','--image','../frames_pieces/'+file], capture_output=True)

                persone_contate += result.stdout.decode().count('person')

                print("Persone contate fino ad ora: "+str(persone_contate))

            print("Ci sono "+str(persone_contate) + " in totale")

        #Prove database
            detection = Detection(
                id_webcam = webcam["id_webcam"],
                city = webcam["city"],
                location = webcam["location"],
                latitude = webcam["latitude"],
                longitude = webcam["longitude"],
                numPeople = persone_contate,
                date = data_dato,
                time = orario,
                type = 0,
                weather_description = weather_description,
                temperature = temperature,
                day_of_week =  datetime.now().date().weekday()
                ).save()
        except:
            time.sleep((t_end - datetime.now()).total_seconds())
    i = 1
    #time.sleep((t_end - datetime.now()).total_seconds())
        #time.sleep(10*60)

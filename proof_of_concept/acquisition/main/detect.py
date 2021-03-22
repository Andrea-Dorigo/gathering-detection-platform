#start with python3 get_video.py
import urllib.request
from urllib.request import urlopen, Request
import os
import time
import string
import glob
import sys
import subprocess
from datetime import datetime
from mongoengine import *
connect("GDP-test", host="localhost", port=27017)

path_frame1 = "../frames_pieces/*.png"
path_video = "../m3u8/"
count = 0
d = 0

lat = 41.899139
long = 12.473311
list_link = []

url_file = open('../link_webcam.txt','r')
for url in url_file.readlines():
    url.split(',')
    list_link.append(url)

#print(list_link)

location = "Piazza Navona"
#urllib.request.urlretrieve(list_link, "../FileMU/PiazzaNavona.m3u8")

files = [os.path.join(path_video, file) for file in os.listdir(path_video) if os.path.isfile(os.path.join(path_video, file))]

class Detection(Document):
    id_webcam = IntField(required=True)
    location = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    numPeople = IntField(required=True)
    date = DateTimeField(required=True)
    time = DateTimeField(required=True)

    def json(self):
        daily_dict = {
            "id_webcam": self.id_webcam,
            "location" : self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "numPeople": self.numPeople,
            "date": self.date,
            "time" : self.time
        }
        return json.dumps(daily_dict) #dumps converte python to json

conta_link = 0
#infinite url request every 1 minutes
while True:
    #orario = datetime.now().time().replace(microsecond=0)
    orario = datetime.now().strftime("%H:%M:%S")
    data_dato = datetime.now().date()
    #download file.m3u8
    #for obj in range(len(list_link)):
    try:
        for conta_link in range (len(list_link)):
            urllib.request.urlretrieve(list_link[conta_link], "../m3u8/PiazzaNavona"+str(conta_link)+".m3u8")
    #    print(list_link[obj])

        i = 0
        list_video = []
    #open & read file.m3u8
        for ffile in files:
            with open(ffile, "r") as fopen:
                for line in fopen.readlines():
                    clean = line[:-1]
                    if clean.endswith('.ts'):
                        #print(clean)
                        if not clean.startswith('https'):
                            clean = 'https://cdn-002.whatsupcams.com/hls/' + clean
                            list_video.append(clean)

                        list_video.append(clean)

        print("List video = ")
        print(list_video)
        print("List video length = ")
        print(len(list_video))


    #download video.ts i=5,7,9,11,13 are the videos location inside lines[]
        for o in range(1):
            urllib.request.urlretrieve(list_video[o], "../videos/Video"+str(o)+".ts")

    #urllib.request.urlretrieve(list_video, "../VideoFontane/Video.ts")

    #extract frame
        exec(open('get_frames.py').read())
    #cut each frames in 6
        exec(open('cut_frame.py').read())
    #call darknet
        conta_persone = 0
        conta_persone2 = 0
        print("after cut_frame")

        for file in glob.glob(path_frame1):
            # bashCommand = "/usr/bin/ls"
            # process = subprocess.Popen(['python3','yolo.py','--image','images/baggage_claim.jpg'],
            #                 stdout=subprocess.PIPE,
            #                 stderr=subprocess.PIPE)
            # output, error = process.communicate()
            # print(output)
            # subprocess.wait()
            result = subprocess.run(['python3','yolo.py','--image','../frames_pieces/'+file], capture_output=True) # running linux ls command
            # print(result.stdout.decode().count('person'))
            conta_persone += result.stdout.decode().count('person')

            #print(subprocess.stoud.readline())

            #subprocess.wait()
            # sys.argv = ['--image images/baggage_claim.jpg --yolo yolo-coco']
            #bashCommand2 = "./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights ../FrameCut/Spagna"+ str(file)
            # process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            #process2 = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
            #process.wait()
            #process2.wait()
            # print("heree")
            # output, error = process.communicate()
            # print(process.returncode)
            #output2, error2 = process2.communicate()
            # conta_persone += output.decode().count('person')
            #conta_persone2 += output.decode().count('person')#3 vs 11su 14
            print("Ci sono "+str(conta_persone)+" in totale")
        #print(conta_persone2)

        a = [1, location, lat, long, conta_persone, data_dato, orario]
        print(a)



    #Prove database
        detection = Detection(
            id_webcam = a[0],
            location = a[1],
            latitude = a[2],
            longitude = a[3],
            numPeople = a[4],
            date = a[5],
            time = a[6]
            ).save()

        time.sleep(60)
    except:
        time.sleep(5)


    #time.sleep(10*60)

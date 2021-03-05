#start with python3 get_video.py

import urllib.request
import os
import time
import string
import glob
import subprocess
from datetime import datetime

bashCommand = "./darknet detect cfg/yolov3.cfg yolov3.weights ../FrameCut/"
#path_frame = "../FrameCut/*.png"
path_frame1 = "../FrameCut/*.png"
path_frame2 = "../FrameCut/Spagna/*.png"
count = 0
d = 0
orario = datetime.now().strftime('%H:%M')
alt = 2
long = 5
data_dato = datetime.now().strftime('%d-%m-%Y')
#list_link = ("https://cdn-002.whatsupcams.com/hls/it_roma02.m3u8", "https://hddn00.skylinewebcams.com/live.m3u8?a=vs0pqlids9c55qqsa2qln4kcq7")
path_video = "../FileMU/"
list_link = "https://cdn-002.whatsupcams.com/hls/it_roma02.m3u8"
#urllib.request.urlretrieve(list_link, "../FileMU/PiazzaNavona.m3u8")


files = [os.path.join(path_video, file) for file in os.listdir(path_video) if os.path.isfile(os.path.join(path_video, file))]

#infinite url request every 5 minutes
while True:
    #download file.m3u8
    #for obj in range(len(list_link)):
    urllib.request.urlretrieve(list_link, "../FileMU/PiazzaNavona.m3u8")
    #    print(list_link[obj])

    i = 0
    list_video = []

    #open & read file.m3u8
    for ffile in files:
        with open(ffile, "r") as fopen:
            for line in fopen.readlines():
                clean = line[:-1]
                if clean.endswith('.ts'):
                    print(clean)
                    if not clean.startswith('https'):
                        clean = 'https://cdn-002.whatsupcams.com/hls/' + clean
                        list_video.append(clean)
                    list_video.append(clean)

    print(list_video)


    #download video.ts i=5,7,9,11,13 are the videos location inside lines[]
    #for o in range(len(list_video)):
    urllib.request.urlretrieve(list_video[0], "../VideoFontane/Video"+str(0)+".ts")

    #urllib.request.urlretrieve(list_video, "../VideoFontane/Video.ts")

    #extract frame
    exec(open('get_frames.py').read())
    #cut each frames in 6
    exec(open('cut_frame.py').read())
    #call darknet
    conta_persone = 0
    conta_persone2 = 0

    for file in glob.glob(path_frame1):
        bashCommand = "./darknet detect cfg/yolov3.cfg yolov3.weights ../FrameCut/"+ str(file)
        #bashCommand2 = "./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights ../FrameCut/Spagna"+ str(file)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        #process2 = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
        process.wait()
        #process2.wait()
        output, error = process.communicate()
        #output2, error2 = process2.communicate()
        conta_persone += output.decode().count('person')
        #conta_persone2 += output.decode().count('person')#3 vs 11su 14
        print(conta_persone)
        #print(conta_persone2)

    a = [alt, long, conta_persone, data_dato, orario]
    print(a)
    time.sleep(10*60)

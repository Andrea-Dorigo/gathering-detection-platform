#start with python3 get_video.py

import urllib.request
import os
import time
import string
import glob
import subprocess

bashCommand = "./darknet detect cfg/yolov3.cfg yolov3.weights ../FrameCut/"
path_frame = "../FrameCut/*.png"
count = 1
d = 0
#list_link = ("https://cdn-002.whatsupcams.com/hls/it_roma02.m3u8", "https://hddn00.skylinewebcams.com/live.m3u8?a=4gsvt3jt5k84e831s2t0snjfo0")
path_video = "../FileMU/"
list_link = "https://hddn00.skylinewebcams.com/live.m3u8?a=arr31505qjgmibjh320dkkp6n2"
urllib.request.urlretrieve(list_link, "../FileMU/PiazzaNavona.m3u8")


files = [os.path.join(path_video, file) for file in os.listdir(path_video) if os.path.isfile(os.path.join(path_video, file))]

#infinite url request every 5 minutes
while True:
    #download file.m3u8
    #for obj in range(len(list_link)):
    urllib.request.urlretrieve(list_link, "../FileMU/PiazzaNavona.m3u8")
        #print(list_link[obj])

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
    #    urllib.request.urlretrieve(list_video[o], "../VideoFontane/Video"+str(o)+".ts")

    urllib.request.urlretrieve(list_video[0], "../VideoFontane/Video"+str(0)+".ts")

    #extract frame
    exec(open('get_frames.py').read())
    #cut each frames in 6
    exec(open('cut_frame.py').read())
    #call darknet
    conta_persone = 0

    for file in glob.glob(path_frame):
        bashCommand = "./darknet detect cfg/yolov3.cfg yolov3.weights ../FrameCut/"+ str(file)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        process.wait()
        output, error = process.communicate()
        conta_persone += output.decode().count('person')
        print(conta_persone)

    print(conta_persone)

    time.sleep(10*60)

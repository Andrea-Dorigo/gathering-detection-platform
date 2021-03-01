import urllib.request
import os
import time
import string
import glob

count = 1
list_link = ("https://hddn00.skylinewebcams.com/live.m3u8?a=4gsvt3jt5k84e831s2t0snjfo0", "https://cdn-002.whatsupcams.com/hls/it_roma02.m3u8")
path_video = "FileMU/"

files = [os.path.join(path_video, file) for file in os.listdir(path_video) if os.path.isfile(os.path.join(path_video, file))]

#infinite url request every 5 minutes

#count perché così posso capire se stanno funzionando i link diversi, col "while true" mi tocca bloccare l'esecuzione del programma
while True:
    #download file.m3u8
    for obj in range(len(list_link)):
        urllib.request.urlretrieve(list_link[obj], "FileMU/fontanaTrevi"+str(obj)+".m3u8")
        print(list_link[obj])

    i = 0
    list_video = []

    #open & read file.m3u8
    for ffile in files:
        with open(ffile, "r") as fopen:
            for line in fopen.readlines():
                clean = line[:-1]
                if clean.endswith('.ts'):
                    if not clean.startswith('https'):
                        clean = 'https://cdn-002.whatsupcams.com/hls/' + clean
                        list_video.append(clean)
                    list_video.append(clean)

    print(list_video)


    #download video.ts i=5,7,9,11,13 are the videos location inside lines[]
    for o in range(len(list_video)):
        urllib.request.urlretrieve(list_video[o], "VideoFontane/Video"+str(o)+".ts")

    #extract frame
    exec(open('get_frames.py').read())

    time.sleep(5*60)

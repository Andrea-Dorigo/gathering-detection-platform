#1)sudo apt-get install python3-pip
#2)python3 -m pip install image_slicer
import glob, os
import image_slicer

count = 0
for file in glob.glob("../Frame/*.jpg"):
    frames=image_slicer.slice(file, 6, save=False)
    image_slicer.save_tiles(frames, directory='../FrameCut/', prefix='slice'+str(count))
    count += 1

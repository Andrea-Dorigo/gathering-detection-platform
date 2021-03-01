#1)sudo apt-get install python3-pip
#2)python3 -m pip install image_slicer
import image_slicer
frame=image_slicer.slice('Frame/frame8.jpg', 6, save=False)
image_slicer.save_tiles(frame, directory='FrameCut/')

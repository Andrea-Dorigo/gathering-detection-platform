#1)sudo apt-get install python3-pip
#2)python3 -m pip install image_slicer
"""
This file is used in get_video.py
The main function cuts all jpgs in the frames folder in 6 parts
for better accuracy in object recognition
"""

import glob
import image_slicer


def cut_frames(PATH_FRAMES, PATH_FRAMES_PIECES):
    """
    This function cuts a frame in 6
    """
    count = 0
    # nframe = 0
    for foto in glob.glob(PATH_FRAMES + "*.jpg"):
        frames = image_slicer.slice(foto, 6, save = False)
        image_slicer.save_tiles(frames, directory = PATH_FRAMES_PIECES, prefix = 'slice'+str(count))
        count += 1

    return True
#cut_frames()
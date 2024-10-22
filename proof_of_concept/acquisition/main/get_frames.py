"""
This file is used in get_video.py
The main function extracts a frame from a ts video
"""

import glob
import cv2
# import requests

def get_frames(PATH_VIDEOS, PATH_FRAMES):
    """
    Extracts a frame from a ts video
    """

    nframe = 0
    for file in glob.glob(PATH_VIDEOS + "*.ts"):
        video_capture = cv2.VideoCapture(file)
        video_capture.set(cv2.CAP_PROP_FPS, 15)

        saved_frame_name = 0
        count = 0

        while video_capture.isOpened() and count < 1:
            frame_is_read, frame = video_capture.read()
            if frame_is_read:
                cv2.imwrite(PATH_FRAMES + "frame" + ".jpg", frame)
                saved_frame_name += 1
                count += 1
                nframe += 1
                statement = True

            else:
                print("Could not read the frame." + count)
                return False

    return bool(statement)
#get_frames()


def extract_frame_from_video_url(video_link):
    frame_is_read, frame = cv2.VideoCapture(video_link).read()
    if frame_is_read:
        # cv2.imwrite("frame.jpg", frame)
        return frame_is_read, frame
    else:
        print("Could not read the frame." + count)

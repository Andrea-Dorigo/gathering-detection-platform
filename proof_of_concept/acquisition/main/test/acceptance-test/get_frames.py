"""
This file is used in get_video.py
The main function extracts a frame from a ts video
"""

import glob
import cv2


def extract_frame_from_video_url(video_link):
    frame_is_read, frame = cv2.VideoCapture(video_link).read()
    if frame_is_read:
        return frame_is_read, frame
    else:
        print("Could not read the frame." + count)

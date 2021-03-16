"""
This file is used in get_video.py
The main function extracts a frame from a ts video
"""

import glob
import cv2

def main():
    """
    Extracts a frame from a ts video
    """

    path = "../VideoFontane/*.ts"
    nframe = 0
    for file in glob.glob(path):
        video_capture = cv2.VideoCapture(file)
        video_capture.set(cv2.CAP_PROP_FPS, 15)

        saved_frame_name = 0
        count = 0

        while video_capture.isOpened() and count < 1:
            frame_is_read, frame = video_capture.read()
            if frame_is_read:
                cv2.imwrite("../Frame/frame"+str(nframe)+".jpg", frame)
                saved_frame_name += 1
                count += 1
                nframe += 1

            else:
                print("Could not read the frame."+count)
                count += 1
main()

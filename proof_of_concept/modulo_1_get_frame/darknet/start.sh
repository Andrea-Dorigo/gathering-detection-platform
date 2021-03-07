#!/bin/sh
systemctl start mongod
python3 get_video.py

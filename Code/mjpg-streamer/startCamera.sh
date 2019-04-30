#!/bin/bash
modprobe bcm2835-v4l2


cd /home/pi/mjpg-streamer/
mjpg_streamer -i "./input_uvc.so -d /dev/video0 -n -y -f 25 -r 640x480" -o "./output_http.so -p 8090 -n -w /usr/local/www"

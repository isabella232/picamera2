#!/usr/bin/python3

# Configure a raw stream and capture an image from it.

from picamera2.picamera2 import *
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.preview_configuration(raw={"size": picam2.sensor_resolution})
print(preview_config)
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

raw = picam2.capture_array("raw")
print(raw.shape)
print(picam2.stream_configuration("raw"))

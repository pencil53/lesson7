import cv2
import numpy as np
import time as t

video = cv2.VideoCapture("download.mp4")
t.sleep(1)
bg = 0
count = 0
for i in range(60):
    return_val,bg = video.read()
    if return_val == False:
        continue

bg = np.flip(bg,axis=1)

while video.isOpened():
    
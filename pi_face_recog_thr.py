from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import numpy as np
import imutils
import cv2
import time
from queue import Queue

cascade_classifiers = {0: "haarcascades/haarcascade_frontalface_default.xml",
                       1: "haarcascades/haarcascade_fullbody.xml",
                       2: "haarcascades/haarcascade_profileface.xml"}

print("Select classifier: \r\n [0]: Frontal face \r\n [1]: Full body \r\n [2]: Profile face \r\n")
try:
    ind=int(input('Choose a number: \r\n'))
except ValueError:
    print("Not a number")
    
cascade = cascade_classifiers[ind]    

cascade = cv2.CascadeClassifier(cascade)

vs = PiVideoStream(resolution=(640,480)).start()
time.sleep(2.0)

fps = FPS().start()

while True:
    image = vs.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    objects = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in objects:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    cv2.imshow('video', image)

    fps.update()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

fps.stop()

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()

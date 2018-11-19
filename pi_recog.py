from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time

cascade_classifiers = [("Frontal face", "haarcascades/haarcascade_frontalface_default.xml"),
                       ("Full body", "haarcascades/haarcascade_fullbody.xml"),
                       ("Profile face", "haarcascades/haarcascade_profileface.xml")]

print("Select classifier:")

for i, t in enumerate(cascade_classifiers):
    print("["+str(i)+"]: " + t[0])

try:
    ind = int(input('Choose a number: \r\n'))
except ValueError:
    print("Error: Not a number")
    exit()
    
try:
    cascade = cascade_classifiers[ind][1] 
except IndexError:
    print("Error: Value out of range")
    exit()

cascade = cv2.CascadeClassifier(cascade)

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    objects = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in objects:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    cv2.imshow('video', image)
    
    rawCapture.truncate(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

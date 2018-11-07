from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

start = time.time()
total_frames = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    cv2.imshow('video',image)
    
    rawCapture.truncate(0)

    total_frames += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


end = time.time()

print(total_frames/(end - start))

cv2.destroyAllWindows()

import numpy as np
import cv2

cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    objects = cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in objects:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    cv2.imshow('video', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()


![agh logo](/home/kamil/Documents/agh.png)



## Image recognition using OpenCV on RaspberryPi

This project is a result of an assignment from an Embedded Systems course. It consists of image recognition scripts written in Python language using OpenCV library (and some others) and code descriptions.

Created in 2019 by Patryk Wójtowicz and Kamil Doległo

 <div style="page-break-after: always;"></div>

# Image recognition

## Code description

```python
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2
import time
```

Firstly, we import some libraries to use later in code.

```python
cascade_classifiers = [("Frontal face", "haarcascades/haarcascade_frontalface_default.xml"),
                       ("Full body", "haarcascades/haarcascade_fullbody.xml"),
                       ("Profile face", "haarcascades/haarcascade_profileface.xml")]
```

Then we declare an array of tuples, which contain description and path to classifier. Classifiers are essentially serialized neural networks. 

```python
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
```

Here we prompt user to select desired classifier, perform some basic validation of input and select this classifier.

```python
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
```

Now we use `PiCamera` library for creating object representation of camera. We set the camera to use resolution 640x480px with framerate of 32 FPS. Then we wait for camera to initialize with sleep(0.1).

```python
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
```

Now we enter a `for` loop, which loops through frames from camera. Frames are in BGR format, which is RGB with swapped blue and red channels. Later we will convert the image from BGR to grayscale for processing, so we would like the most to get a frame in grayscale in the first place. Unfortunately, the camera doesn't support a grayscale mode. 

```python
image = frame.array
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Here we take the actual image matrix from frame and convert it to grayscale.

```python
objects = cascade.detectMultiScale(gray, 1.3, 5)
```

Now we use the neural network for detecting objects, passing the frame and additional parameters - scaleFactor of 1.3 and minNeighbors of 5. Scale factor specifies how much the image size is reduced at each image scale, because every frame is scaled down in steps and then each scaled image is an input to the neural network. This process increases the chance of a match. Min neighbours parameter specifies how many neighbors each candidate rectangle should have to retain it. This parameter will affect the quality of the detected faces: higher value results in less detections but with higher quality.

That's how we detect objects: with just one line of code!

```python
for (x,y,w,h) in objects:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]

    cv2.imshow('video', image)
```

The detectMultiScale() function returns coordinates of rectangle for each detected object, so now we draw these rectangles on the image and display it on screen. 

```python
rawCapture.truncate(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

```

truncate(0) function flushes the image stream from camera, so that we process only frames that we are able to process in real time. If we omitted this call, we would process each frame from camera, so the displayed video would be delayed (because the Raspberry Pi can process images at about 2 FPS and the input stream has a framerate of 32 FPS) and finally, out frame buffer would overflow. 

Then we just check if the user pressed 'q' key on the keyboard and if so, we break from the loop. 

```python
camera.close()
cv2.destroyAllWindows()

```

Finally, we release the camera and destroy the window in which processed frames were displayed. 

 <div style="page-break-after: always;"></div>

# Training haar cascades

## Prepare samples

To train your own cascade you'll need samples both positive and negative. Negative samples you have to provide yourself, while positive samples can be generated from the negative ones and a single image of an object you want to detect. 

So let's say you provided 2000 negative samples (preferably small images like 100x100 and in grayscale) and an object image (50x50 also in grayscale). To generate positive examples you also need a background file (bg.txt), describing the negative dataset.

So if we have a directory structure like this:

```
neg/
  --img1.jpg
  --img2.jpg
bg.txt
target_img.jpg
pos/
data/
```

ur bg.txt file needs to look like:

```
neg/img1.jpg
neg/img2.jpg
```

To generate postive examples we can use opencv_createsamples utility provided by opencv. To do that, run the command in the workspace directory like this:

```bash
$ opencv_createsamples -img target_img.jpg -bg bg.txt -info info.lst -pngoutput pos -maxxangle 0.1 -maxyangle 0.1 -maxzangle 0.1
```

(you can look up the meaning of the options here: https://docs.opencv.org/2.4.13.2/doc/user_guide/ug_traincascade.html)

Then you need to create a single vector file from these positive samples like this:

```bash
$ opencv_createsamples -info info.lst -num 2000 -w 20 -h 20 positives.vec
```

We shrink the image to 20x20 for optimisation, we can experiment with these values

## Train the dataset

Data directory is where we keep the data about each epoch of the training.

To train the data set you need to run this:

```bash
$ opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
```

We do the 2:1 ratio of positive images to negative images (supposedly the best ratio). Number of the images is not 2000, because with each epoch the training set grows)

After the training, you should have a `cascade.xml` file in your data directory, which you can use in your opencv script.

#### Sources

- https://docs.opencv.org/2.4.13.2/doc/user_guide/ug_traincascade.html
- https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/




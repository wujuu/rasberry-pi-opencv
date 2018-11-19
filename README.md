# Image recognition using Raspberry Pi

This repository contains demos of object recognition on a Raspberry Pi using an official camera with Python and OpenCV library. 

## Getting started

Scripts were written for Raspberry Pi 3 B+ and its official serial interface camera. It should be possible to run them on another version of Raspberry, but the framerate may be unacceptable. 

Scripts depend on Python >= 3 and OpenCV >= 3, and use NumPy, PiCamera and Imutils libraries.  

To install OpenCV, you have three options:

1. (recommended) Run `pip install opencv`, which should fetch and set up OpenCV. If you don't have pip, you’ll need to obtain it first:

   ```bash
   $ wget https://bootstrap.pypa.io/get-pip.py
   $ sudo python3 get-pip.py
   $ pip install opencv
   ```

2. Compile OpenCV yourself. Good article on how to do that is there:  [https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/)

3. Flash your SD card with `opencv.iso`. Note that this image is intended to use on Raspberry Pi 3 B+, other Raspberry Pi versions may not work with it. 

You also need to install required libraries (they are already preinstalled on the  `opencv.iso` image):

```bash
$ pip install numpy, picamera, imutils
```

This command should fetch and install them. 

You can now run the scripts:

```bash
$ python3 pi_recog.py
```



## Files description

`pi_recog` file is a basic script with 3 predefined Haar cascades from OpenCV.

`pi_recog_threaded` file is essentially the same script, but uses imutils library for capturing images in a separate thread and FPS measurement. 


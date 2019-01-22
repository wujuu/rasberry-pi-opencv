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

If you use official RaspberryPi camera then for running `recog_simplest.py` script you also need to load a kernel module for the camera:

```bash
$ sudo modprobe bcm2835_v4l2 
```

You can now run the scripts:

```bash
$ python3 pi_recog.py
```



## Files description

* `recog_simplest.py` file is the simplest version of image recognition using OpenCV. This script requires the `bcm2835_v4l2` kernel module.

* `pi_recog.py` file is a basic script with 3 predefined Haar cascades from OpenCV.

* `pi_recog_threaded.py` file is essentially the same script, but uses `imutils` library for capturing images in a separate thread and FPS measurement. 

* `haarcascades/` directory contains classifiers for things like face or full body detection. Those files are taken from OpenCV library. 

## Links

- Repository: <https://github.com/wujuu/rasberry-pi-opencv>
- Issue tracker: <https://github.com/wujuu/rasberry-pi-opencv/issues>
- Related projects:
  - Object detection based on TensorFlow: <https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/>
  - OpenCV optimized for Raspberry Pi 3: <https://github.com/abhiTronix/OpenCV_Raspberry_pi_TBB/>

## Authors

- **Patryk Wójtowicz** - *Initial work, scripts, training cascades* - [wujuu](https://github.com/wujuu)
- **Kamil Doległo** - *OpenCV image and documentation* - [kamilok1965](https://github.com/kamilok1965)

## Licensing

This project is licensed under the MIT license
## Scary TV Triggered by Computer Vision

This project uses a Raspberry Pi 3, OpenCV and the MediaPipe pose detection model to trigger a scary portrait on a smart TV. 

When the model detects that someone has sat down in front of the TV, the code triggers a portrait to come to life and scare the person. 

The code keeps triggering as long as a person's two shoulder landmarks are detected. Hold up one hand to stop the video. If the model detects that your wrist is above your shoulder, the video will stop playing and the code will terminate.

This setup uses a cellphone camera that's connected to the Raspberry Pi via wifi. Because the camera is not plugged into the Raspberry Pi or into the TV, you have the flexibility to place it anywhere.

By placing the camera low down and pointing it at a very specific location you will ensure that the video will only trigger if a person is seated in one specfic place. People walking around the room will not trigger the video because the upper part of their bodies will not appear on the camera.

<br>

#### When the model detects a person, this is what happens:

<br>
<img src="https://github.com/vbookshelf/Scary-TV-Triggered-by-Computer-Vision/blob/main/images/scare-portrait5.gif" width="500"></img>
<i>Videos were purchased from AtmosFX.<br>
Two videos were combined and edited to create this video.<br>
The video also has sound.</i>

<br>

<br>

### Hardware I used

- Raspberry Pi 3 A+
- Android cellphone
- Samsung smart TV
- TP-Link home wifi router

<br>


### How to run this project

- Connect the Raspberry Pi to the TV using an HDMI cable.<br>

- Install OpenCV and MediaPipe. I've included a pdf file that sets out the installation steps that worked for me.
- Install the Omxplayer-wrapper:<br>
$ sudo python3 -m pip install omxplayer-wrapper

- Install imutils<br>
$ sudo pip3 install imutils

- Install the Android app on the cellphone. Please refer to this tutorial:<br>
https://www.youtube.com/watch?v=lXeiicHhtNs
- Start the server on the Android app. Change the IP address in scary-tv-code-rev1.py to match the IP address given in the app. Both the Raspberry Pi and the cellphone need to be connected to the same wifi network.

- Due to copyright, I've not included the scary video in this repo. There is a sample video of a dog. You can use it to test that everything is working.
- Upload the scare-tv-folder to the Raspberry Pi.


- Using the command line, cd into scare-tv-folder. 
- Run the python file. The paused video should appear on the TV screen.<br>
$ python3 scary-tv-code-rev1.py

- Point the camera at a person - that should trigger the video to start playing.
- If the person raises his or her hand, and holds it up for a few seconds, that will stop the code and close the video player.
- Also, you can press Press Ctrl C to stop the code.

<br>

### Lessons Learned

- Set the GPU memory on the Raspberry Pi to 128. At 64 (the default setting) there is no sound.<br>
Preferences --> Raspberry Pi Configuration --> Performance --> GPU Memory
- The code can be a little unstable - the video may not pause at exactly the same place each time.
- The wifi camera app works surprisingly well and having the flexibility to place the camera anywhere is very helpful.

<br>

## Reference Resources

- scarethetots<br>
Living Portrait Scare for Halloween Using a Raspberry Pi, PIR and Python<br>
https://www.instructables.com/Raspberry-Pi-Based-Living-Portrait-Player-Intro/

- Nick Marino<br>
Halloween Raspberry Pi 3 B Project Possessed Portrait<br>
https://www.youtube.com/watch?v=IWHBdU4OHOY

- MediaPipe Pose<br>
https://google.github.io/mediapipe/solutions/pose

- pantechsolutions<br>
Camera interface with RPi - USB | Mobile Camera<br>
(Explains how to connect a cellphone camera to a computer (or Raspberry Pi) via wifi.<br>
This is helpful if you don't have a USB webcam or a Raspberry Pi camera.)<br>
https://www.youtube.com/watch?v=lXeiicHhtNs

- IP Webcam Android app<br>
https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_ZA&gl=US

- Murtaza's Workshop - Robotics and AI<br>
Latest Pose Estimation Realtime (24 FPS) using CPU | Computer Vision | OpenCV Python 2021<br>
https://www.youtube.com/watch?v=brwgBf6VB0I

- vbookshelf Repo<br>
Raspberry Pi Resources for Beginners<br>
https://github.com/vbookshelf/Raspberry-Pi-Resources-for-Beginners


<br>

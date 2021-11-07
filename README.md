## Scary TV Triggered by Computer Vision

In progress...

This project uses a Raspberry Pi 3, OpenCV and the MediaPipe pose detection model to trigger a scary portrait on a smart TV. 

When the model detects that someone has sat down in front of the TV, the code triggers a portrait to come to life and scare the person. 

The code keeps triggering as long as a person's two shoulder landmarks are detected. To stop the video hold up one hand. If the model detects that your wrist is above your shoulder, the video will stop playing and the code will terminate.

This setup uses a cellphone camera that's connected to the Raspberry Pi via wifi. Because the camera is not plugged into the Raspberry Pi or into the TV, you have the flexibility to place it anywhere.

Placing the camera low down and close to where the person needs to sit, means that the person will have to be sitting before his or her shoulders will appear on camera - people walking around the room will not trigger the code.

<br>

#### When the model detects a person, this is what happens:
(The video also has sound.)

<br>
<img src="https://github.com/vbookshelf/Scary-TV-Triggered-by-Computer-Vision/blob/main/images/scare-portrait5.gif" width="500"></img>
<i>Videos were purchased from AtmosFX</i>
<br>

<br>


### How to run this project

- Install OpenCV and MediaPipe. I've included a pdf file that sets out the installation steps that worked for me.
- Install the Omxplayer-wrapper:
$ sudo python3 -m pip install omxplayer-wrapper
- Install the Android app on the cellphone:
https://www.youtube.com/watch?v=lXeiicHhtNs

- Put the video and the Python script into the same folder. I've not included the scary video in this repo due to copyright. There is a sample video of a dog.
- Connect the Raspberry Pi to the TV using the HDMI cable
- Upload the folder to the Raspberry Pi.
- Start the server on the Android app. Change the IP address in the python code to match the IP address given in the app. Both the Raspberry Pi and the cellphone need to be connected to the same wifi network.

- Using the command line, cd into the directory containing the python code and the video.
- Run the python file:
$ python3 my_python_file.py

- If you point the camera at a person that should trigger the video.
- If the person raises his or her hand, that will stop the code.
- Also, you can press Press Ctrl C to stop the code.

<br>

### Lessons Learned

- Set the GPU memory on the Raspberry Pi to 128. At 64 (the default setting) there is no sound.

<br>

## Reference Resources

- scaretots<br>
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

- Murtaza's Workshop - Robotics and AI<br>
Latest Pose Estimation Realtime (24 FPS) using CPU | Computer Vision | OpenCV Python 2021<br>
https://www.youtube.com/watch?v=brwgBf6VB0I

- vbookshelf Repo<br>
Raspberry Pi Resources for Beginners<br>
https://github.com/vbookshelf/Raspberry-Pi-Resources-for-Beginners


<br>

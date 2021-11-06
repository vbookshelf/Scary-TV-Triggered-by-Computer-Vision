## Scary TV Triggered by Computer Vision

In progress...

This project uses a Raspberry Pi 3, OpenCV and the MediaPipe pose detection model to trigger a scary portrait on a smart TV. 

When the model detects that someone has sat down in front of the TV, the code triggers a portrait to come to life and scare the viewer. 

The code keeps triggering as long as a person's two shoulder landmarks are detected. To stop the video hold up one hand. If the model detects that your wrist is above your shoulder, the video will stop playing and the code will terminate.

This setup uses a cellphone camera thats connected to the Raspberry Pi via Wifi. Because the camera is not plugged into the Raspberry Pi or into the TV, you have the flexibility to place it anywhere.

Placing the camera low down and close to where the person needs to sit, means that the person will have to be sitting before his or her shoulders will appear on the camera - people walking around the room will not trigger the code.

<br>

#### When the model detects a person, this is what happens:
(The video also has sound.)

<br>
<img src="https://github.com/vbookshelf/Scary-TV-Triggered-by-Computer-Vision/blob/main/images/scare-portrait5.gif" width="500"></img>
<i>Videos were purchased from AtmosFX</i>
<br>

<br>

### Background

### How this project works

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

- vbookshelf Repo<br>
Raspberry Pi Resources for Beginners<br>
https://github.com/vbookshelf/Raspberry-Pi-Resources-for-Beginners


<br>

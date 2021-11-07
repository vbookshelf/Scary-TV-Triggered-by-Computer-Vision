
# Notes:
# ......

# 1- This code is based on the orginal code created by scarethetots:
# https://www.instructables.com/Raspberry-Pi-Based-Living-Portrait-Player-Intro/

# 2- Start the server on the Android app before running this code.
# 3- The video, this code and the my_cv_utils_rev0.py file need to be in the same folder.



import cv2
import mediapipe as mp
import numpy as np
import time
import serial

import sys
from omxplayer.player import OMXPlayer
from time import sleep


import urllib.request
import imutils 

# Import helper functions from my_cv_utils_rev0.py
# I suggest that you take a look at the functions in this file.
from my_cv_utils_rev0 import *



##################################

# This is the IP address given in the Android app.
# Change this to match the address given by your app.
url = 'http://192.168.0.104:8080/shot.jpg'

# This is the video file name.
# Change this to match your video file name.
VIDEO_PATH = 'dog-sample-video3.mp4'

#VIDEO_PATH = 'scare-video5.mp4'

##################################

# You may need to adjust these values to suit your TV screen size.
slength = '1440'
swidth = '900'

video_width = 640



mp_pose = mp.solutions.pose
pose = mp_pose.Pose() # there are parameters that can be entered here

print("Starting...")



try:
	
	# initialize the video player
	player = OMXPlayer(VIDEO_PATH,  args=['--no-osd', '--loop', '--win', '0 0 {0} {1}'.format(slength, swidth)])
	sleep(1)
	print("Ready to trigger")
	
	start_time = 0

	while True:
		
		
		# This must be placed right at the top
		player.pause()
	
		
		# Get the image frame from the cellphone camera
		image = get_image_from_cellphone_camera(url, video_width)
		
		# flip the image so that it's like looking in a mirror.
		image = cv2.flip(image, 1)
		
		# Convert the image from BGR to RGB.
		# MediaPipe uses RGB images.
		image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		
		# process the image and store the results in an object
		results = pose.process(image_rgb)
		
		#print(results.pose_landmarks)
	
		
		# if a person has been detected
		if results.pose_landmarks:
			
			x_list = []
			y_list = []
			
			
			# Extract each coord
			
			# By following this link you will find a diagram that shows which index values
			# correspond to which points on the body:
			# https://google.github.io/mediapipe/solutions/pose
			# The origin point (0,0) on images is in the top left corner.
			
			for id, lm in enumerate(results.pose_landmarks.landmark):
				
				# get the height, width and number of channels
				h, w, c = image.shape
				
				
				# Get the x and y coords of each landmark.
				# The coords of each landmark are specified as a ratio of the image size.
				# We need to convert that ration into a length.
				cx = int(lm.x * w)
				cy = int(lm.y * h)
				
				# Add the x and y coords to a list.
				# The position in the list corresponds to the landmark number e.g.
				# landmark 12 is at x_list[12].
				x_list.append(cx)
				y_list.append(cy)
				
				
				# These are the landmarks that we will be using:
				# -- shoulders and wrists
				# 11 - left_shoulder
				# 12 - right_shoulder
				# 15 - left_wrist
				# 16 - right_wrist
	
			if len(y_list) != 0:
				
				# To stop the video raise you left or right hand and hold it up for a while.
				# If your wrist is above your shoulder then the video will stop.
				# We use less than (<) because the origin (0,0) is in the top left corner.
				if (y_list[15] < y_list[11]) or (y_list[16] < y_list[12]):
					
					print('Goodbye')
					player.quit()
					sys.exit()
						
						
				elif len(y_list) > 0:
						
					# Trigger the video
					print('Triggering video')
					player.play()
					sleep(player.duration())
					
				else:
					# This part looks redundant but it's important.
					# Without this the video does not automatically
					# appear when the code starts. And it terminates 
					# unexpectedly when a person is not detected.
					pass
					
							
				player.set_position(0.0)
					
			
			
		# If the camera does not detect a person.		
		else:
			
			print("No person detected")
			
		

# Press Ctrl C to end the program.			
except KeyboardInterrupt:
	print('Goodbye')
	player.quit()
	sys.exit()

	
		
		
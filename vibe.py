
#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
import subprocess

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
 
print("------------------")
print(" OMXPlayer + GPIO ")
print("------------------")
 
print("--------------")
print(GPIO.input(17))
print(GPIO.input(27))
print(GPIO.input(22))
print("--------------")

video_playing = False
video_playing2 = False
video_playing3 = False
video_playing4 = False
omxc = None

while True:
        # read states of inputs
        # REPLACE THE FOLLOWING 3 LINES WITH THE LINES FROM read.py ON THE ARDUINO. THEY HAVE BEEN ADAPTED FOR THE TYPES OF SENSORS IN THE MODEL.
        # here it is assumed: input_state1(GPIO 27) is plant; input_state2(GPIO 22 is human); input_state3(GPIO 17 is cat). CHANGE THE PIN NUMBERS ACCORDING TO REAL PINS IN THE MODEL.
        input_state1 = GPIO.input(27)
        input_state2 = GPIO.input(22)
        input_state3 = GPIO.input(17)
        
        # logic for playing the soothing nature video - if video is not playing and only the plant is in the room.
        if ( not video_playing and input_state1 and not (input_state2 and input_state3)):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video soothing nature>', shell=True, preexec_fn=os.setsid)
            video_playing = True
            video_playing2 = False
            video_playing3 = False
            video_playing4 = False
                
        # logic for playing the traffic video - if video is not playing and human is in the room. 
        if ( not video_playing2 and input_state2):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video trafic infernal>', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = True
            video_playing3 = False
            video_playing4 = False

        # logic for playing the cat video - if video is not playing and cat is in the room but not the human. we define all combinations.
        only_cat = input_state3 and not input_state1 and not input_state2
        cat_plant = input_state3 and input_state1 and not input_state2
        if ( not video_playing3 and (only_cat or cat_plant)):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video trafic infernal>', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = False
            video_playing3 = True
            video_playing4 = False

        # logic for when no sensors are activated. use new video for when no objects are in the room, or use existing video(like soothing nature), or delete the whole block and a black screen will be displayed.
        if ( not video_playing4 and not input_state1 and not input_state2 and not input_state3):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video idle>', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = False
            video_playing3 = False
            video_playing4 = True

            
        # here we check if the omxc player which plays the video is stopped in which case the flag variables are reset so the video starts playing again creating a loop until something changes in the sensor configuration.
        if omxc.poll() is not None: 
            video_playing = False
            video_playing2 = False
            video_playing3 = False
            video_playing4 = False


                
            

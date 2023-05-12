
#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
import subprocess

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
print("------------------")
print(" OMXPlayer + GPIO ")
print("------------------")
 
print("--------------")
print(GPIO.input(17))
print(GPIO.input(27))
print(GPIO.input(22))
print(GPIO.input(23))
print("--------------")

video_playing = False
video_playing2 = False
omxc = None

while True:
        # read states of inputs
        input_state1 = GPIO.input(27)
        input_state2 = GPIO.input(22)
        input_state3 = GPIO.input(23)
        input_state4 = GPIO.input(17)
        
        # logic for playing the idle video - if video is not playing and not all sensors are activated.
        if ( not video_playing and not(input_state1 and input_state2 and input_state3 and input_state4)):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/PUCK_intro.mp4', shell=True, preexec_fn=os.setsid)
            video_playing = True
            video_playing2 = False
                
        # logic for playing the active video - if video is not playing and all sensors are activated.
        if (not video_playing2 and input_state1 and input_state2 and input_state3 and input_state4):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/monolog_PUCK.mp4', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = True
            
        # here we check if the omxc player which plays the video is stopped in which case the flag variables are reset so the video starts playing again creating a loop until something changes in the sensor configuration.
        if omxc.poll() is not None: 
            video_playing = False
            video_playing2 = False


                
            


#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
import subprocess

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# configure sensor pins. if some sensors are not triggering even if the LEDs are reacting(may be a different sensor model), try removing the pull_up_down=GPIO.PUD_UP parameter like this GPIO.setup(17, GPIO.IN) 
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
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
omxc = None

while True:
        # read states of inputs
        # here it is assumed: input_state1(GPIO 27) is photo1; input_state2(GPIO 22 is photo2); input_state3(GPIO 17 is photo3). CHANGE THE PIN NUMBERS ACCORDING TO REAL PINS IN THE MODEL.
        input_state1 = GPIO.input(27)
        input_state2 = GPIO.input(22)
        input_state3 = GPIO.input(17)
        
        # logic for playing the video 1.
        if ( not video_playing and input_state1):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video photo 1>', shell=True, preexec_fn=os.setsid)
            video_playing = True
            video_playing2 = False
            video_playing3 = False
        
        # logic for playing the video 2.
        if (not video_playing2 and input_state2):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video photo 2>', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = True
            video_playing3 = False

        # logic for playing the video 3.
        if (not video_playing3 and input_state3):
            subprocess.call("pkill omx", shell=True)
            omxc = subprocess.Popen('omxplayer /home/pi/Documents/Fagaras/<video photo 3>', shell=True, preexec_fn=os.setsid)
            video_playing = False
            video_playing2 = False
            video_playing3 = True
            
        # if no sensors are activated, no video is playing.

        # here we check if the omxc player which plays the video is stopped in which case the flag variables are reset so the video starts playing again creating a loop until something changes in the sensor configuration.
        if omxc.poll() is not None: 
            video_playing = False
            video_playing2 = False
            video_playing3 = False


                
            

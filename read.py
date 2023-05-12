
#!/usr/bin/env python
 
from time import sleep
import os
import RPi.GPIO as GPIO
import sys
import subprocess

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# configure sensor pins. if some sensors are not triggering even if the LEDs are reacting(may be a different sensor model), try removing the pull_up_down=GPIO.PUD_UP parameter like this GPIO.setup(17, GPIO.IN) 
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
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
omxc = None

reset1=True
reset2=True
reset3=True
reset4=True
reset0=True

while True:
        #Read states of inputs
        input_state1 = GPIO.input(27)
        input_state2 = GPIO.input(22)
        input_state3 = GPIO.input(23)
        input_state4 = GPIO.input(17)

        if input_state1 and reset1:
            print(1)
            reset1 = False
            reset2 = True
            reset3 = True
            reset4 = True
            reset0 = True
        if input_state2 and reset2:
            print(2)
            reset1 = True
            reset2 = False
            reset3 = True
            reset4 = True
            reset0 = True
        if input_state3 and reset3:
            print(3)
            reset1 = True
            reset2 = True
            reset3 = False
            reset4 = True
            reset0 = True
        if input_state4 and reset4:
            print(4)
            reset1 = True
            reset2 = True
            reset3 = True
            reset4 = False
            reset0 = True
        elif not input_state1 and not input_state2 and not input_state3 and not input_state3 and reset0:
            print(0)
            reset1 = True
            reset2 = True
            reset3 = True
            reset0 = False
        
            

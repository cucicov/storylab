# storylab

## TODO:
- on other raspberry pies then puck the following should be done:
  - set black desktop background: https://www.radishlogic.com/raspberry-pi/change-desktop-background-of-raspberry-pi/#:~:text=If%20you%20want%20to%20change,on%20the%20filename%20beside%20Picture%20.
  - hide task bar above: Right click on the Menu bar and select Panel Settings.. Go to Advanced Tab.. Tick Automatic Hiding and set size when minimised to 0 pixels.
  
# Utilities
CTRL+ALT+T - open terminal

- file read.py can be used for tests, it prints 1/2/3/4 for each of the sensors activated and 0 if no sensors are activated. To run it open terminal window and type **python \<full path to the file\>**

- For PUCK, video plays continuously and cannot be stopped. Use **CTRL+ALT+T** to open terminal in the background and type **sudo pkill python** and then **ENTER**. This will kill python script at the end of the playing video. Do this even if you dont see the terminal opening and the video is still playing, it will do all the things in the background. 

- to make the script auto start at the launch on raspberry pi use **Method 1: rc.local** (https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)
  - open terminal
  - sudo nano /etc/rc.local
  - add this before the line **exit 0** at the end of the file: **sudo python /home/pi/\<full path to the file\>**
  - CTRL + X
  - Y
  - ENTER
  - sudo reboot

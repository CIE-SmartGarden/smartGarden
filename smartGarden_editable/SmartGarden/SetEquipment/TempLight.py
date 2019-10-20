import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *

def LightControl(tempVal):
    GrowLight()
    if tempVal < 25:
        LightBulb(True) #Turn on Grow Light
    elif tempVal > 40:
        Fan(True) # Turn on Fan
    else:
        Fan(False)
        LightBulb(False) #Turn off Light Bulb & Fan
        
def GrowLight():
    hour = int(strftime("%H", localtime()))
    if hour in range(5,22):
        pass #turn on Grow Light
    else:
        pass #turn off Grow Light
        
def Fan(_open):
    if _open:
        pass #turn on fan
    else:
        pass #turn off fan
    
def LightBulb(_open):
    if _open:
        pass #turn on Grow Light 
    else:
        pass #turn off Grow Light
    
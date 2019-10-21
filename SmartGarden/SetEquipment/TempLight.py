import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *

def LightControl():
    GrowLight()
#     if tempVal < 25:
#         LightBulb(True) #Turn on Grow Light
#     elif tempVal > 40:
#         Fan(True) # Turn on Fan
#     else:
#         Fan(False)
#         LightBulb(False) #Turn off Light Bulb & Fan
def GrowLight():
    hour = int(strftime("%H", localtime()))
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    GPIO.setup(light_relay, GPIO.OUT)
    if hour in range(5,22):
        print("LED ON!!!")
        return GPIO.output(light_relay, 0)
    else:
        print("LED OFF!!!")
        return GPIO.output(light_relay, 1)
# def Fan(_open):
#     if _open:
#         pass #turn on fan
#     else:
#         pass #turn off fan
#     
# def LightBulb(_open):
#     if _open:
#         pass #turn on Grow Light 
#     else:
#         pass #turn off Grow Light
    

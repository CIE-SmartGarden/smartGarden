import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *

def GrowLight():
    hour = int(strftime("%H", localtime()))
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    if hour in range(5,22):
#         print("LED ON!!!")
        return GPIO.output(light_relay, 0)
    else:
#         print("LED OFF!!!")
        return GPIO.output(light_relay, 1)
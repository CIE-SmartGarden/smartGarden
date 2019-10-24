import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *

async def GrowLight(StartTime, StopTime):
    hour = int(strftime("%H", localtime()))
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    if hour in range(StartTime, StopTime+1):
#         print("LED ON!!!")
        GPIO.output(light_relay, 0)
    else:
#         print("LED OFF!!!")
        GPIO.output(light_relay, 1)
    
    return True
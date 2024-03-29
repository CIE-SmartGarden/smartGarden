import RPi.GPIO as GPIO
from time import sleep, time, strftime, localtime
from datetime import *
import asyncio

async def GrowLight(command, light_relay ,StartTime=0, StopTime=0):

    if command:
        hour = int(strftime("%H", localtime()))
        
        if hour in range(StartTime, StopTime+1):
            GPIO.output(light_relay, 0)
            
        else:
            GPIO.output(light_relay, 1)

        return True
    else:
        GPIO.output(light_relay, 1)
        return False
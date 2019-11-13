import RPi.GPIO as GPIO
from time import sleep
import asyncio

async def HeatControl(command, fan_relay ,tempVal=0, maxTemp=0, minTemp=0):
    
    if command: 
        if tempVal > maxTemp: 
            return await FanBlow(True, fan_relay)
        elif tempVal < minTemp:
            await FanBlow(False, fan_relay)
            pass # Heat up # Fan Close
            return
        else:
            await FanBlow(False, fan_relay)
            pass # Heat close # Fan Close
            return
    else:
        await FanBlow(False, fan_relay)
        pass # Heat close # Fan Close
        return
    
async def FanBlow(command, fan_relay):
#     GPIO.setmode(GPIO.BCM)
#     fan_relay = 25
#     GPIO.setwarnings(False)
#     GPIO.setup(fan_relay, GPIO.OUT)
    if command:
        GPIO.output(fan_relay, 0)
        return True
    else:
        GPIO.output(fan_relay, 1)
        return False

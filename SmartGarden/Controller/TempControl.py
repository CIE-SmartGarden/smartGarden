import RPi.GPIO as GPIO
from time import sleep
import asyncio

async def HeatControl(command, fan_relay, heat_relay, tempVal=0, maxTemp=0, minTemp=0):
    
    if command: 
        if tempVal > maxTemp:
            await FanBlow(True, fan_relay)
            await HeatPad(False, heat_relay)
            return True
        
        elif tempVal < minTemp:
            await FanBlow(False, fan_relay)
            await HeatPad(True, heat_relay)
            return True
        
        else:
            await FanBlow(False, fan_relay)
            await HeatPad(False, heat_relay)
            return True
        
    else:
        await FanBlow(False, fan_relay)
        await HeatPad(False, heat_relay)
        return False
    
async def FanBlow(command, fan_relay):

    if command:
        GPIO.output(fan_relay, 0)
        return True
    
    else:
        GPIO.output(fan_relay, 1)
        return False

async def HeatPad(command, heat_relay):
    
    if command:
        GPIO.output(heat_relay, 0)
        return True
    
    else:
        GPIO.output(heat_relay, 1)
        return False
    
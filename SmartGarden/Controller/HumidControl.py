import RPi.GPIO as GPIO
import threading
import asyncio

async def WaterControl(command, pump_relay, humVal=0, minHum=0, seconds=2): # open valve for 2 sec
    
    if command:
        
        if humVal < minHum:
            return await WaterPump(seconds, pump_relay) 
        
        else:
            GPIO.output(pump_relay, 1)
            
        await asyncio.sleep(seconds)
        return True
    
    else:
        
        GPIO.output(pump_relay, 1)
        return False
    
async def WaterPump(seconds, pump_relay):
    
    GPIO.output(pump_relay, 0)
    await asyncio.sleep(seconds)
    GPIO.output(pump_relay, 1)
    
    return True

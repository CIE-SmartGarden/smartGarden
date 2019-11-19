import RPi.GPIO as GPIO
import asyncio
from hx711py.weight import get_weight

async def mapping(val, maxval):
    return 100 - (val/maxval)*100

async def checkHumidity(mcp):
    values = mcp.read_adc(4)
    result = round(await mapping(values, 1023), 2)
    return result

async def WaterPump(seconds, pump_relay):
    GPIO.output(pump_relay, 0)
    await asyncio.sleep(seconds)
    GPIO.output(pump_relay, 1)

async def WaterControl(command, pump_relay, minHum, hx, mcp)
    humVal = checkHumididy(mcp)
    waterVal = 
    
    if command:
        if humVal < minHum:
            return await WaterPump(2, pump_relay) # open valve for 2 sec
    else:
        GPIO.output(pump_relay, 1)
        
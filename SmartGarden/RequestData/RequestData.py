'''
import serial
import struct
import asyncio
data = serial.Serial('/dev/ttyACM0', 115200)

async def checkHumidity():
    i = "h".encode() #Arduino is ascii, python is unicode
    data.write(i)
    while True:
        if (data.in_waiting > 0):
            result = data.readline()
            humiVal = float(result.strip().decode("utf-8"))
            return humiVal
        await asyncio.sleep(0.01)
        
async def checkTemperature():
    i = "t".encode() #Arduino is ascii, python is unicode
    data.write(i)
    while True:
        if (data.in_waiting > 0):
            result = data.readline()
            tempVal = float(result.strip().decode("utf-8"))
            return tempVal
        await asyncio.sleep(0.01)
'''

import sys
import Adafruit_DHT
import asyncio
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time
import asyncio

async def checkTemperature(sensor=Adafruit_DHT.DHT22, pin=4):# Parse command line parameters.
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if temperature is not None:
        return temperature
    
    else:
        print('Failed to Read Temperature')
        return ''

async def mapping(val, maxval):
    return 100 - (val/maxval)*100
    
async def checkHumidity(mcp):
    values = mcp.read_adc(0)
    result = round(await mapping(values, 1023), 2)
    return result 

async def weight(hx):   
    val = hx.get_weight(5) 
    hx.power_down()
    hx.power_up()
    return float(val)

async def checkWaterLevel(hx):
    return round(await weight(hx), 2)


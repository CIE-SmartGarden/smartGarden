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

async def checkTemperature(sensor=Adafruit_DHT.DHT22, pin=4):# Parse command line parameters.
    
#     sensor_args = { '11': Adafruit_DHT.DHT11,
#                     '22': Adafruit_DHT.DHT22,
#                     '2302': Adafruit_DHT.AM2302 }
#     
#     if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
#         sensor = sensor_args[sys.argv[1]]
#         pin = sys.argv[2]
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    
    if temperature is not None:
        print('Temp={0:0.1f}  '.format(temperature))
        return temperature
    
    else:
        print('Fail to Read')
        return ''
#     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#     if temperature is not None:
#         print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#         return temperature

# checkTemperature()
asyncio.get_event_loop().run_until_complete(checkTemperature())


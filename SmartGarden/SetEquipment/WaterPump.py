import RPi.GPIO as GPIO
from time import sleep
import asyncio

plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

waterTypes = { "xeric" : [20,29] ,
               "mesic" : [30,49] ,
               "hydric" : [50,60] 
                }

async def WaterControl(humVal, minHum):
#     print('Value:', min(waterTypes[plantDict["plantA"]["waterType"]]))
    if humVal < minHum:
#         print("humidity ==> ",humVal)
        return await WaterPump(2) # 5 sec is time for openning valve
    
async def WaterPump(seconds):
    
    GPIO.setmode(GPIO.BCM)
    pump_relay = 26
    GPIO.setwarnings(False)
    GPIO.setup(pump_relay, GPIO.OUT)

#     GPIO.output(pump_relay, 1)
#     sleep(1)
#     try:
    GPIO.output(pump_relay, 0)
    await asyncio.sleep(seconds)
    GPIO.output(pump_relay, 1)
    
    return True
#     print("I pump for", seconds , "secs!")
#     except KeyboardInterrupt:
#          print("I except na")
    


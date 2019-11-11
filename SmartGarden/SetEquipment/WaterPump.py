import RPi.GPIO as GPIO
import threading
import asyncio

async def WaterControl(command, pump_relay, waterVal, humVal=0, minHum=0):
 
#     GPIO.setmode(GPIO.BCM)
#     pump_relay = 26
#     GPIO.setwarnings(False)
#     GPIO.setup(pump_relay, GPIO.OUT)
    
    if command:
        if waterVal < 30:
            print("The water tank is now at critical level")
#             return

        if humVal < minHum:
            return await WaterPump(2, pump_relay) # open valve for 2 sec
        
    else:
        GPIO.output(pump_relay, 1)
        
    return
    
async def WaterPump(seconds, pump_relay):
#     GPIO.setmode(GPIO.BCM)
#     pump_relay = 26
#     GPIO.setwarnings(False)
#     GPIO.setup(pump_relay, GPIO.OUT)
    GPIO.output(pump_relay, 0)
    await asyncio.sleep(seconds)
    GPIO.output(pump_relay, 1)
    return True

# WaterPump(1)
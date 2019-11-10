import RPi.GPIO as GPIO
import threading
import asyncio

async def WaterControl(command, humVal=0, minHum=0, watertank):
    
#     GPIO.setmode(GPIO.BCM)
#     pump_relay = 26
#     GPIO.setwarnings(False)
#     GPIO.setup(pump_relay, GPIO.OUT)
    
    if command:
        if watertank < 30:
            print("The water tank is now at critical level")
            return

        if humVal < minHum :
            return await WaterPump(2) # open valve for 2 sec

    else:
        GPIO.output(pump_relay, 1)
        
    return
    
async def WaterPump(seconds):
#     GPIO.setmode(GPIO.BCM)
#     pump_relay = 26
#     GPIO.setwarnings(False)
#     GPIO.setup(pump_relay, GPIO.OUT)
    GPIO.output(pump_relay, 0)
    await asyncio.sleep(seconds)
#        Water_Pump_Wait(seconds,pump_relay)
    GPIO.output(pump_relay, 1)
    return True

# WaterPump(1)
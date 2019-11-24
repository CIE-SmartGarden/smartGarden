from picamera import PiCamera
from time import sleep
from datetime import *
import asyncio

async def camera():
    today = datetime.now()
    
    camera = PiCamera()
    camera.resolution = (320,240)
    
    camera.start_preview()
    camera.capture('/home/pi/Desktop/smartGarden/SmartGarden/Pictures/'+str(today)+'.jpg')
    camera.stop_preview()
    camera.close()
    
    return today

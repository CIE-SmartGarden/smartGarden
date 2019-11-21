from picamera import PiCamera
from time import sleep
from datetime import *
import asyncio

async def camera():
    today = datetime.now()
    camera = PiCamera()
    camera.start_preview()
    camera.capture('/home/pi/Desktop/smartGarden/SmartGarden/'+str(today)+'.jpg')
    camera.stop_preview()
    return today

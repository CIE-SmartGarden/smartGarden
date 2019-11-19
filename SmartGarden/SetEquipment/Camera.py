from picamera import PiCamera
from time import sleep
from datetime import *
import asyncio

async def camera():
    today = datetime.now()
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/Picture/'+str(today)+'.jpg')
    camera.stop_preview()


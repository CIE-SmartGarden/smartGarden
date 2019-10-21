from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import writeFile
from datetime import *
import time
import asyncio
import threading

def main():
    
    threading.Timer(30, main).start() # run every 30 secs
    
    humVal = checkHumidity()
    WaterControl(humVal)
    
    tempVal = checkTemperature()
    HeatControl(tempVal)
    
    GrowLight()
    
#     print("hum",humVal)
#     print("tem",tempVal)
    writeFile(humVal, tempVal)
    
    print("time stamp ==> ","date",datetime.now().strftime("%d:%m:%y"),"time",datetime.now().strftime("%H:%M:%S"))

main()

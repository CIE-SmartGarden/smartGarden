from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight,LightControl
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import writeFile
from datetime import *
import time
import asyncio
import threading

now = datetime.now()

def main():
    timer = 15
    threading.Timer(timer, main).start() # run every 600 secs
#
    humVal = checkHumidity()             # check humidity
    print("check hum checked")
    WaterControl(humVal)                 # use humid_val to run pump
    print("WaterControl checked")
#     tempVal = checkTemperature()
#     LightControl(tempVal)
    tempVal = checkTemperature()
    print("Temp check")
    HeatControl(tempVal)
    GrowLight()
#     print("hum",humVal)
#     print("tem",tempVal)
    writeFile(humVal, tempVal)
    print("time warped ==> ","date",now.strftime("%d:%m:%y"),"time",now.strftime("%H:%M:%S"))

main()

from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight, LightBulb, LightControl
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import writeFile
from datetime import *
import time
import asyncio
import threading

plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperatePlant', "waterType": 'mesic'}
                }

waterTypes = { "xeric" : 20 ,
               "mesic" : 30 ,
               "hydric" : 50 
                }

tempTypes = {  "tropical" : 20 ,
               "temporate": 15 ,
                }

def main():
    threading.Timer(5.0, main).start() # run every 300 secs
#     
    humVal = checkHumidity()             # check humidity
    print("check hum passed")
    WaterControl(humVal)                 # use humid_val to run pump
    print("WaterControl passed")
#     
#     tempVal = checkTemperature()
#     LightControl(tempVal)
    tempVal = checkTemperature()
    print("Heat check")
    HeatControl(tempVal)
#     
#     print("hum",humVal)
#     print("tem",tempVal)
#     writeFile(humVal, tempVal)
# 
    GrowLight()
    print("GrowLight passed")
    print("5 Min passed ")
main()

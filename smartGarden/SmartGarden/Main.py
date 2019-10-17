from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight, LightBulb, LightControl
from editfiles import writeFile 
import time
import asyncio
import threading

def main():
    
    threading.Timer(5.0, main).start() #run every 5 minutes
    
    humVal = checkHumidity()
    WaterControl(humVal)
    tempVal = checkTemperature()
    LightControl(tempVal)
    
    print("hum",humVal)
    print("tem",tempVal)
    writeFile(humVal, tempVal)


main()
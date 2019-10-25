from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import writeFile
from datetime import *
import time
import asyncio
import threading

async def main(command, maxTemp=0, minTemp=0, maxHum=0, minHum=0, timeStart=0, timeStop=0):
    
    #threading.Timer(5, main).start() # run every 30 secs   
    if command == True:
        humVal = await checkHumidity()
        await WaterControl(humVal, minHum)
        tempVal = await checkTemperature()
        await HeatControl(tempVal, maxTemp, minTemp)
        await GrowLight(timeStart, timeStop)
        print("hum",humVal)
        print("tem",tempVal)
        await writeFile(humVal, tempVal)
        await asyncio.sleep(3)
    
    else:
        print('stop the controller')
        return

    #print("time stamp ==> ","date",datetime.now().strftime("%d:%m:%y"),"time",datetime.now().strftime("%H:%M:%S"))

# while True:
#     asyncio.get_event_loop().run_until_complete(main())

#    asyncio.get_event_loop().run_forever()

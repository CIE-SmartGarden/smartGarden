from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import writeFile, checkFile2
from datetime import *
import time
import threading

def main(command=False):
    
    threading.Timer(5, main).start() # run every 30 secs
    
    if checkFile2() != []:
        command = True
        data = checkFile2()
        maxTemp, minTemp, maxHum, minHum, timeStart, timeStop = int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6])
    else: command = False
    
    if command:
        humVal = checkHumidity()
        WaterControl(command, humVal, minHum)
        tempVal = checkTemperature()
        HeatControl(tempVal, maxTemp, minTemp)
        GrowLight(command, timeStart, timeStop)
        print("hum",humVal)
        print("tem",tempVal)
        writeFile(humVal, tempVal)

    else:
        WaterControl(command)
        GrowLight(command)
        FanBlow(command)
    
main()

    #print("time stamp ==> ","date",datetime.now().strftime("%d:%m:%y"),"time",datetime.now().strftime("%H:%M:%S"))

# while True:
#     asyncio.get_event_loop().run_until_complete(main())

#    asyncio.get_event_loop().run_forever()

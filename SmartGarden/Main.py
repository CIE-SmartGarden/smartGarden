from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl, FanBlow 
from editfiles import writeFile, checkFile
from datetime import *
from hx711py.weight import weight
import time
import threading
import asyncio

async def controller():
    
    while True:
#     threading.Timer(5, main).start() # run every 5 secs
        command=False
        if await checkFile() != []:
            command = True
            data = await checkFile()
            maxTemp, minTemp, maxHum, minHum, timeStart, timeStop = int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6])
        
        if command:
            print('running')
            watertank = await weight()
           humVal = await checkHumidity()
            await WaterControl(command, humVal, minHum, watertank)
           tempVal = await checkTemperature()
            await HeatControl(command, tempVal, maxTemp, minTemp)
            await GrowLight(command, timeStart, timeStop)
#             print("hum",humVal)
#             print("tem",tempVal)
            await writeFile(humVal, tempVal)


        else:
            await WaterControl(command)
            await GrowLight(command)
            await FanBlow(command)
            await HeatControl(command)
            print('stop')
            
        await asyncio.sleep(5)
        
# def ps1():
#     main()

    #print("time stamp ==> ","date",datetime.now().strftime("%d:%m:%y"),"time",datetime.now().strftime("%H:%M:%S"))

# while True:
#     asyncio.get_event_loop().run_until_complete(main())

#    asyncio.get_event_loop().run_forever()

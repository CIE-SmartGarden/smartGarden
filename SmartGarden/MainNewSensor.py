from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl, FanBlow 
from editfiles import writeFile, checkFile
from datetime import *
from hx711py.weight import weight
from RequestData.MoistureSensor import moisture
from RequestData.TemperatureSensor import Temp, Temperature
import time
import threading
import asyncio
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

async def startingController():
    '''Setup weight sensor'''
    EMULATE_HX711=False
    if not EMULATE_HX711:
        import RPi.GPIO as GPIO
        from hx711py.hx711 import HX711
    else:
        from hx711py.emulated_hx711 import HX711
    hx = HX711(5,6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(-423.3)
    hx.reset()
    hx.tare()
    temporal = await weight(hx)
    waterVal = round(temporal, 2)
    print("Done setup weight sensor")
    
    
    '''Setup temperature sensor'''
    tempVal = -274
    while tempVal == -274:
        tempVal = await Temp(tempVal)
    print("Done setup temp sensor")
        
    '''Setup moisture sensor'''
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    humVal = await moisture()
    print("Done setup weight sensor")
    
    print(waterVal, tempVal, humVal)
    
    '''Setup all GPIO pin'''
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    fan_relay = 25
    pump_relay = 26
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    GPIO.setup(fan_relay, GPIO.OUT)
    GPIO.setup(pump_relay, GPIO.OUT)
    
    while True:
        asyncio.get_event_loop().run_until_complete(controller())

        asyncio.get_event_loop().run_forever()
    
async def controller():
    
    while True:
#     threading.Timer(5, main).start() # run every 5 secs
        command=False
        if await checkFile() != []:
            command = True
            data = await checkFile()
            maxTemp, minTemp, maxHum, minHum, timeStart, timeStop = int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6])
            print("The data is empty")
            
        if command:
            print('running')
#            humVal = await checkHumidity()
            await WaterControl(command, humVal, minHum)
#            tempVal = await checkTemperature()
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


asyncio.get_event_loop().run_until_complete(startingController())
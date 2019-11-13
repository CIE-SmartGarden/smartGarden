from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl, FanBlow 
from editfiles import writeData, readFile
from datetime import *
from hx711py.weight import weight
from RequestData.RequestData import checkTemperature, checkHumidity, checkWaterLevel
from RequestData.MoistureSensor import moisture
from RequestData.TemperatureSensor import Temp, Temperature
import time
import threading
import asyncio
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

async def setupController():
    
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    fan_relay = 25
    pump_relay = 26
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    GPIO.setup(fan_relay, GPIO.OUT)
    GPIO.setup(pump_relay, GPIO.OUT)
    
    '''Setup weight sensor'''
    EMULATE_HX711=False
    if not EMULATE_HX711:
        from hx711py.hx711 import HX711
    else:
        from hx711py.emulated_hx711 import HX711
    hx = HX711(5,6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(-423.3)
    hx.reset()
    hx.tare()
    
    '''Setup temperature sensor'''
#     prevTemp = -274
#     while prevTemp == -274:
#         prevTemp = await Temp(prevTemp)
#     print("Done setup temp sensor")
        
    '''Setup moisture sensor'''
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    
    return int(light_relay), int(fan_relay), int(pump_relay), hx, mcp
    
async def controller():
    
    light_relay, fan_relay, pump_relay, hx, mcp = await setupController()
    
    command = False
    
    while True:
        
        
        
        if await readFile('check.csv') != []:
            
            prevTemp = -274
            while prevTemp == -274:
                prevTemp = await Temp(prevTemp)

            frequencyChecking=5
            fre = await readFile('ifconfig.csv')
            if fre != []: frequencyChecking = int(fre[0][0])
            print('freCheck:', frequencyChecking)
            
            data = await readFile('check.csv')
            command = True
            maxTemp, minTemp, maxHum, minHum, timeStart, timeStop = int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6])
            
            
            while command:
                
                if await readFile('check.csv') == []:
                    command = False
                    break
                
                print('running')
                
# #                 threading.Timer(frequencyChecking, main).start() # run every 5 secs                        
#                 
#                 waterVal = await checkWaterLevel(hx)
# #                 print("Weight of water tank",waterVal)
                humVal = await checkHumidity(mcp)
#                 await WaterControl(command, pump_relay, waterVal, humVal, minHum)
# #                 tempVal = await checkTemperature()
                tempVal = await Temp(prevTemp)
#                 await HeatControl(command, fan_relay, tempVal, maxTemp, minTemp)
#                 await GrowLight(command, light_relay, timeStart, timeStop)
                await writeData([humVal, tempVal])
#                 print("hum",humVal)
#                 print("tem",tempVal)

                prevTemp = tempVal
                await asyncio.sleep(frequencyChecking)
        
        print('stop')
        
#         waterVal = await checkWaterLevel(hx)
#         await WaterControl(command, pump_relay, waterVal)
#         await GrowLight(command, light_relay)
#         await FanBlow(command, fan_relay)
#         await HeatControl(command, fan_relay)
        
        
        await asyncio.sleep(1)
        
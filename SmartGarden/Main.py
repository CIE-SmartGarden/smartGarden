from Controller.HumidControl import WaterPump, WaterControl
from Controller.GrowlightControl import GrowLight
from Controller.TempControl import HeatControl, FanBlow, HeatPad 
from editfiles import readFile
from datetime import *
from RequestData.hx711py.weight import get_weight
from RequestData.RequestData import checkTemperature, checkHumidity, checkWaterLevel
from RequestData.MoistureSensor import moisture
from RequestData.TemperatureSensor import Temp, Temperature
import websockets
import time
import threading
import asyncio
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

async def setupController():
    
    """ Setup GPIO """
    GPIO.setmode(GPIO.BCM)
    light_relay = 23
    fan_relay = 25
    pump_relay = 26
    heat_relay = 24
    GPIO.setwarnings(False)
    GPIO.setup(light_relay, GPIO.OUT)
    GPIO.setup(fan_relay, GPIO.OUT)
    GPIO.setup(pump_relay, GPIO.OUT)
    GPIO.setup(heat_relay, GPIO.OUT)
    
    '''Setup weight sensor'''
    EMULATE_HX711=False
    if not EMULATE_HX711:
        from RequestData.hx711py.hx711 import HX711
    else:
        from RequestData.hx711py.emulated_hx711 import HX711
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
    
    return int(light_relay), int(fan_relay), int(pump_relay), int(heat_relay), hx, mcp
    
async def controller(pin=1234):

    light_relay, fan_relay, pump_relay, heat_relay, hx, mcp = await setupController()
    command = False
    frequencyChecking=5
    
    checkFile = 'check['+ str(pin) + '].csv'
    settingFile = 'ifconfig['+ str(pin) + '].csv'
    
    while True:
        
        if await readFile(checkFile) != []:
            prevTemp = -274
            
            while prevTemp == -274:
                prevTemp = await Temp(prevTemp)
#             frequencyChecking=5
#             fre = await readFile(settingFile)
#             if fre != []: frequencyChecking = int(fre[0][0])
#             print('freCheck:', frequencyChecking)
            data = await readFile(checkFile)
            command = True
            maxTemp, minTemp, maxHum, minHum, timeStart, timeStop = int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6])
            
            while command:
                
                if await readFile(checkFile) == []: break
                
                print('running')
#                 threading.Timer(frequencyChecking, main).start() # run every 5 secs                        
                
                """ Water Control System"""
                waterVal = await get_weight(hx)
                humVal = await checkHumidity(mcp)
                await WaterControl(command, pump_relay, humVal, minHum)

                """ Temperature Control System """
#                 tempVal = await checkTemperature()
                tempVal = await Temp(prevTemp)
                await HeatControl(command, fan_relay, heat_relay, tempVal, maxTemp, minTemp)
                
                """ Growlight Control System """
                await GrowLight(command, light_relay, timeStart, timeStop)
                
                """ Storing Data """
                await sentData(str([humVal, tempVal, waterVal]), str(pin))
#                 await writeData([humVal, tempVal, waterVal])
#                 print("hum",humVal)
#                 print("tem",tempVal)
                
                prevTemp = tempVal
                await asyncio.sleep(frequencyChecking-2)
                
        print('stop')

        if command:
            command = False
#             waterVal = await checkWaterLevel(hx)
            await WaterControl(command, pump_relay)
            await GrowLight(command, light_relay)
            await HeatControl(command, fan_relay, heat_relay)
        
        await asyncio.sleep(1)
        
async def sentData(data, pin):
    
    async with websockets.connect('ws://0.0.0.0:5679') as websocket:
        
        await websocket.send(pin)
        await websocket.recv()
        await websocket.send(data)
        await websocket.recv()

asyncio.get_event_loop().run_until_complete(controller())

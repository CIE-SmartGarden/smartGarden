from RequestData.RequestData import checkHumidity, checkTemperature
from SetEquipment.WaterPump import WaterPump, WaterControl
from SetEquipment.TempLight import GrowLight
from SetEquipment.FanControl import HeatControl , FanBlow 
from editfiles import readFile, writeFile, writeCheck, checkFile, deleteFile
from datetime import *
import time
import asyncio
import threading
import websockets

async def response(websocket, path):
    
    if await checkFile() != []:

        data = await checkFile()
        await main(True, int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6]))
        
#         print('check:', await checkFile())
        message = await websocket.recv()
        print("We got message from client:", message)
        
        if message == 'data':
            dataCollection = await readFile('data.csv')
            if len(dataCollection) == 0:
                await websocket.send("no data")
                
            else:
                await websocket.send(str(dataCollection))
                
    #         await websocket.send((20).to_bytes(2, byteorder="little"))
        
        elif message == 'stop':
            await deleteFile('check.csv')
            await deleteFile('data.csv')
            await main(False)
            await websocket.send('Stop!')
            
        else:
            await websocket.send("Please try again")        

        await asyncio.sleep(10)
        
    else:
        
#         print('checkElse:', await checkFile())
        
        message = await websocket.recv()        
        
        if message == 'plant':
            await websocket.send('Give your plant name')
            plant_name = await websocket.recv()
            a = await find_plant(plant_name)
            if a == False:
                await websocket.send('Incorrect Input')
                
            else:
                await deleteFile('data.csv')
                await writeCheck(a)
                await websocket.send('Start!')
                data = await checkFile()
                await main(True, int(data[0][1]),int(data[0][2]),int(data[0][3]),int(data[0][4]),int(data[0][5]),int(data[0][6]))
                
        
        else:
            if message == 'data':
                await websocket.send("no data")
            elif message == 'stop':
                await websocket.send("the machine already stop")
            else:
                print(message)
                await websocket.send("Please try again")
            
                
                
async def find_plant(plant_name):
    plantData = await readFile('database.csv')
    for row in plantData:
        if plant_name == row[0]:
            return row
    return False
            
            
            
async def main(command, maxTemp=0, minTemp=0, maxHum=0, minHum=0, timeStart=0, timeStop=0):
    
    #threading.Timer(5, main).start() # run every 30 secs   
    if command == True:
        humVal = await checkHumidity()
        await WaterControl(True, humVal, minHum)
        tempVal = await checkTemperature()
        await HeatControl(tempVal, maxTemp, minTemp)
        await GrowLight(True, timeStart, timeStop)
        print("hum",humVal)
        print("tem",tempVal)
        await writeFile(humVal, tempVal)

    else:
        await WaterControl(False)
        await GrowLight(False)
        await FanBlow(False)
    
# '''TEST'''
# def server_run():
#     start_server = websockets.serve(response, '172.17.1.139', 5678)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()
    start_server = websockets.serve(response, '172.17.1.139', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
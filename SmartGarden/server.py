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

#         print('check:', await checkFile())
#         async for message in websocket:
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
            await websocket.send('Stop!')
            
        else:
            await websocket.send("Please try again")        

#         await asyncio.sleep(10)
        
    else:
        
#         print('checkElse:', await checkFile())
#         async for message in websocket:
        message = await websocket.recv()        
        print("We got message from client:", message)
        
        if message == 'plant':
            await websocket.send('Give your plant name')
            plant_name = await websocket.recv()
            print("client's plant:", plant_name)
            a = await find_plant(plant_name)
            if a == False:
                await websocket.send('Incorrect Input')
                
            else:
                await deleteFile('data.csv')
                await writeCheck(a)
                await websocket.send('Start!')
        
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
            
            
    
# '''TEST'''
# def server_run():
#     start_server = websockets.serve(response, '172.17.1.139', 5678)
#     asyncio.get_event_loop().run_until_complete(start_server)
#     asyncio.get_event_loop().run_forever()
start_server = websockets.serve(response, '0.0.0.0', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
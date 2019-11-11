from editfiles import readFile, writeFile, writeCheck, checkFile, deleteFile
from datetime import *
from oldMain import setupController, controller
import time
import asyncio
import threading
import websockets

async def response(websocket, path):
    
    if await checkFile() != []:

        message = await websocket.recv()
        print("We got message from client:", message)
        
        if message == 'data':
            dataCollection = await readFile('data.csv')
            if len(dataCollection) == 0:
                await websocket.send("no data")
                
            else:
                await websocket.send(str(dataCollection))
                        
        elif message == 'stop':
            await deleteFile('check.csv')
            await deleteFile('data.csv')
            await websocket.send('Stop!')
            
        else:
            await websocket.send("Please try again")        
        
    else:
    
        message = await websocket.recv()        
        print("We got message from client:", message)
        
        if message == 'start':
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
                await websocket.send("Please try again")        
                
async def find_plant(plant_name):
    
    plantData = await readFile('database.csv')
    for row in plantData:
        if plant_name == row[0]:
            return row
        
    return False

try:
    start_server = websockets.serve(response, '0.0.0.0', 5678)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.create_task(controller())
    loop.run_forever()

except (KeyboardInterrupt, SystemExit):
    GPIO.cleanup()
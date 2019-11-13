from editfiles import readFile, writeFile, deleteFile
from datetime import *
from Main import setupController, controller
import time
import asyncio
import threading
import websockets
import RPi.GPIO as GPIO


async def response(websocket, path):
    
    if await readFile('check.csv') != []:

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
        
        elif message == 'setting':
            await websocket.send('What do you want to do?')
            setting = await websocket.recv()
            if setting == 'frequent checking':
                frequency = await websocket.recv()
                if int(frequency) < 5:
                    await websocket.send('Please give more than or equal to 5 sec')
                    return 
                await writeFile('ifconfig.csv', [frequency])
                await websocket.send('Please restart your device')
            elif setting == 'reset':
                await deleteFile('ifconfig.csv')
                await websocket.send('Please restart your device')
            else:
                await websocket.send('Please try again')
                
        else:
            await websocket.send("Please try again")        
        
    else:
    
        message = await websocket.recv()        
        print("We got message from client:", message)
        
        if message == 'start':
            await websocket.send('Give your plant name')
            plant_name = await websocket.recv()
            print("client's plant:", plant_name)
            plantData = await find_plant(plant_name)
            if plantData == False:
                await websocket.send('Sorry, that plant\'s name is not included')
                
            else:
                await deleteFile('data.csv')
                await writeFile('check.csv', plantData)
                await websocket.send('Start!')
                
        elif message == 'setting':
            await websocket.send('What do you want to do?')
            setting = await websocket.recv()
            if setting == 'frequent checking':
                frequency = await websocket.recv()
                print('frequecy:', frequency)
                if int(frequency) < 5:
                    await websocket.send('Please give more than or equal to 5 sec')
                    return 
                await writeFile('ifconfig.csv', [frequency])
                await websocket.send('Done')
            elif setting == 'reset':
                await deleteFile('ifconfig.csv')
                await websocket.send('Done')
            else:
                await websocket.send('Please try again')
                
        elif message == 'data':
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
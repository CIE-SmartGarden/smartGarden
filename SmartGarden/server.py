from editfiles import readFile, writeFile, writeData, deleteFile, find_data
from base64 import b64encode, decodestring, decodebytes
from datetime import *
from Controller.Camera import camera
from encoding import decodePicture
import time
import ast 
import asyncio
import threading
import websockets
import RPi.GPIO as GPIO


async def response(websocket, path):
    
    start = False
    pin = await websocket.recv()
    start = await find_data(pin, 'controllerPin.csv')
    
    if not start:
        await websocket.send('Invaild pin, please try again')
        return
    
    await websocket.send('Access!')
    
    if await readFile('check.csv') != []:     
        
        message = await websocket.recv()
        
        if message[0] == '[' and message[-1] == ']':
            data = ast.literal_eval(message)
            await writeData(data)
#             print("hum",data[0])
#             print("tem",data[1])
            return True
        else:    
            print("We got message from client:", message)
        
        if message == 'data':
            
            dataCollection = await readFile('data.csv')
            
            if len(dataCollection) == 0:
                await websocket.send("no data")
                
            else:
                await websocket.send(str(dataCollection))
        
        elif message == 'water level':
            
            waterLevel = await readFile('data.csv')
            waterPercent = float(waterLevel[-1][-1])/10
            waterPercent = round(waterPercent, 3)
            
            if waterPercent < 30:
                msg = "The water tank is now at critical level [water level: "+ str(waterPercent) +"%]"
                
            else:
                msg = "The water tank is now "+ str(waterPercent)+ "%"
                
            await websocket.send(msg)
                
        elif message == 'stop':
            await deleteFile('check.csv')
            await deleteFile('data.csv')
            await websocket.send('Stop!')
            
        elif message == 'camera':
            name = await camera()
            code = await decodePicture(name)
            await websocket.send(str(code))
                
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
            PlantList = [i[0] for i in await readFile('database.csv')]
            del PlantList[0]
            await websocket.send(str(PlantList))
            plant_name = await websocket.recv()
            print("client's plant:", plant_name)
            plantData = await find_data(plant_name, 'database.csv')
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
        
        elif message == 'water level' or message == 'camera':
            await websocket.send("Please start the machine")
    
        elif message == 'data':
            await websocket.send("no data")
        
        elif message == 'stop':
            await websocket.send("the machine already stop")
        
        else:
            await websocket.send("Please try again")        
                



start_server = websockets.serve(response, '0.0.0.0', 5679)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
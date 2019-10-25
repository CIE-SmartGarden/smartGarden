from editfiles import readFile
import asyncio
import websockets

async def response(websocket, path):
    
    message = await websocket.recv()
    print("We got message from client:", message)

    if message == 'data':
        dataCollection = await readFile('data.csv')
        if len(dataCollection) == 0:
            await websocket.send("no data")
            return False
        else:
            await websocket.send(str(dataCollection))
            return True
#         await websocket.send((20).to_bytes(2, byteorder="little"))

    elif message == 'plant':
        await websocket.send('Give your plant name')
        plant_name = await websocket.recv()
        a = await find_plant(plant_name)
        if a == False:
            await websocket.send('Incorrect Input')
        else:
            f = open('data.csv','w+')
            f.close()
            await websocket.send(str(a))
    
    elif message == 'stop':
        await websocket.send('False')
            
    else:
        await websocket.send("Please try again")


async def find_plant(plant_name):
    plantData = await readFile('database.csv')
    for row in plantData:
        if plant_name == row[0]:
            return row
    return False
            
            
start_server = websockets.serve(response, '0.0.0.0', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
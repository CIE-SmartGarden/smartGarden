import asyncio
import websockets
import ast 

async def message():
    async with websockets.connect('ws://127.0.0.1:5678') as websocket:
        msg = input("What do you want to request: ")
        if msg == 'plant':
            plant = input("What plant do you want: ")
            await websocket.send(plant)
            print(await websocket.recv())
        elif msg == 'data':
            await websocket.send(msg)
            res = ast.literal_eval(await websocket.recv()) #convert to str to list
            print(res)
#             print(int.from_bytes(await websocket.recv(), "little"))
        else:
            await websocket.send(msg)
            print(await websocket.recv())
        

asyncio.get_event_loop().run_until_complete(message())
#asyncio.get_event_loop().run_forever()
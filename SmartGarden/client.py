from Main import main
import asyncio
import websockets
import ast 

start = False

async def message():
    
    async with websockets.connect('ws://127.0.0.1:5678') as websocket:
        
        msg = input("What do you want to request: ")

        if msg == 'data':
            await websocket.send(msg)
            check = await websocket.recv()
            if check == "no data":
                print('no data')
                return False
            else:
                dataCollection = ast.literal_eval(check)
                print(dataCollection) #convert to str to list
                return dataCollection
#             print(int.from_bytes(await websocket.recv(), "little"))

        elif msg == 'plant':
            await websocket.send(msg)
            print(await websocket.recv())
            plant = input("What plant do you want: ")
            await websocket.send(plant)
            message = await websocket.recv()
            if message == 'Incorrect Input':
                print('Sorry, that plant\'s name is not included')
                return False
            else:
                print(ast.literal_eval(message))
                return ast.literal_eval(message)
        
        else:
            await websocket.send(msg)
            print(await websocket.recv())
            return False

data = asyncio.get_event_loop().run_until_complete(message())

# print(data)
#asyncio.get_event_loop().run_forever()

if type(data) == list: # problem is the check variable list problem (if it go to 'data' statement), cannot go out the loop should run separate 
    if len(data) == 7:
        while True:
            asyncio.get_event_loop().run_until_complete(main(int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6])))

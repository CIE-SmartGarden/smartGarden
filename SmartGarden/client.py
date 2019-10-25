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
                return [True, ast.literal_eval(message)]
        
        elif msg == 'stop':
            await websocket.send(msg)
            check = await websocket.recv()
            return [False]
        
        else:
            await websocket.send(msg)
            print(await websocket.recv())
            return False

check = asyncio.get_event_loop().run_until_complete(message())

# print(data)
#asyncio.get_event_loop().run_forever()

if type(check) == list: # problem is the check variable list problem (if it go to 'data' statement), cannot go out the loop should run separate 
    if type(check[0]) == bool:
        if check[0] == True:
            data = check[1]
            while True:
                asyncio.get_event_loop().run_until_complete(main(True, int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6])))
        else:
            asyncio.get_event_loop().run_until_complete(main(False))
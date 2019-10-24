from Main import main
import asyncio
import websockets
import ast 

start = False

async def message():
    
    async with websockets.connect('ws://127.0.0.1:5678') as websocket:
        
        msg = input("What do you want to request: ")
        
        if msg == 'plant':
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
            
        elif msg == 'data':
            await websocket.send(msg)
            print(ast.literal_eval(await websocket.recv())) #convert to str to list
            return True
#             print(int.from_bytes(await websocket.recv(), "little"))

        else:
            await websocket.send(msg)
            print(await websocket.recv())
            return False

check = asyncio.get_event_loop().run_until_complete(message())
start, data = check[0], check[1]
# print(data)
#asyncio.get_event_loop().run_forever()

if start == True: # problem is the check variable list problem (if it go to 'data' statement), cannot go out the loop should run separate 
    while True:
        asyncio.get_event_loop().run_until_complete(main(int(data[1]),int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6])))

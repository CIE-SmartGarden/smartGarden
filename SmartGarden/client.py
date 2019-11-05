import asyncio
import websockets
import ast 

async def message():
    
    async with websockets.connect('ws://0.0.0.0:5678') as websocket:
        
        msg = input("What do you want to request: ")
        await websocket.send(msg)
        check = await websocket.recv()
        
        if msg == 'data':
            if check == 'no data': print(check)
                #return False
            else:
                dataCollection = ast.literal_eval(check)
                print(dataCollection) #convert to str to list
                #return dataCollection

        elif msg == 'plant':
            if check == 'Please try again': print('already plant!')
                #return False
            plant = input("What plant do you want: ")
            await websocket.send(plant)
            message = await websocket.recv()
            if message == 'Incorrect Input':
                print('Sorry, that plant\'s name is not included')
                #return False
            else: print(message)
                #return True
        else: print(check)
            #return False
    
asyncio.get_event_loop().run_until_complete(message())
asyncio.get_event_loop().run_forever()

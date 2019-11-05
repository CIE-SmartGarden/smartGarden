
from multiprocessing import Process
import time
import asyncio

async def kuy1():
    print('kuy1')
    
async def kuy2():
    print('kuy2')
    
p1 = Process(target=kuy1)
p2 = Process(target=kuy2)


p1.start() # spawn process
p2.start()

p1.join()  # blocks until done
p2.join()

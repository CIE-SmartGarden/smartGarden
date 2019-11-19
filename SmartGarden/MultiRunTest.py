from Main import ps1
from server import ps2
from multiprocessing import Process
import time
import asyncio
    

p1 = Process(target=ps1)
p2 = Process(target=ps2)


p1.start() # spawn process
p2.start()

p1.join()  # blocks until done
p2.join()

import time
import signal
import Adafruit_DHT
from multiprocessing import Process
import asyncio

class BlntReadError(Exception):
    pass

def timeout(signum, frame):
    raise BlntReadError('took too long')

signal.signal(signal.SIGALRM, timeout)

def getSen(pin_x):
    
    temperature = -274
    start = time.time()
    signal.alarm(1)
    
    try:
        humid,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,pin_x)
    except BlntReadError:
        print('action timed out!')
        
    signal.alarm(0)
    
    
    if temperature is None or temperature == -274:
        return None
    
    if temperature is not None:
        temperature = round(temperature, 3)
        print(temperature,"before end_val","pin",pin_x)
#        print("\n")
        return temperature

# def getCon(pin):
#     
#     pc = Process(target=getSen,args =(pin,))
#     pc.start()
#     pc.join()

def getTemp():
    
    p1 = Process(target=getSen, args=(4,))
    p2 = Process(target=getSen, args=(20,))
    p3 = Process(target=getSen, args=(21,))
    
    p1.start() # spawn process
    p2.start()
    p3.start()
# 
    p1.join()  # blocks until done
    p2.join()
    p3.join()

    result = []
    
    end_result = list(filter(None,result))  
#      
    if len(end_result) == 0:
        return False
#          
    end_val = round(sum(filter(None,result)) / len(end_result),3)
    print("-------")
    print(end_val)
    return end_val

# getTemp()


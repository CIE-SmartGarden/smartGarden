#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT
# sensor = Adafruit_DHT.DHT22
# pin = 4

#humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
import time
import signal
import asyncio
# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

class BlntReadError(Exception):
    pass

def timeout(signum, frame):
    raise BlntReadError('took too long')

signal.signal(signal.SIGALRM, timeout)

async def Temperature(pin=20):
    
    start = time.time()
    temperature = -274
    
    signal.alarm(1)
    
    try:
        humid,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,pin)
    except BlntReadError:
#         print('action timed out!')
        pass
        
    signal.alarm(0)
    
    temperature = round(temperature, 3)

    return temperature

async def Temp(prevTemp):
    t = await Temperature()
    if t == -274:
        t = prevTemp
    return t


# out = -274
# errorcount = 0
# totalcount = 0
# while True:
#     try:
#         t = Temperature()
#         if t != -274:
#             out = t
#             print("CHANGE")
#         if t == -274:
#             errorcount += 1
#         time.sleep(1)
#         print(out)
#         totalcount += 1
#         print("TOTAL = " + str(totalcount) + "\nERROR = " + str(errorcount))
#         print("Error percentage", (errorcount/totalcount * 100))
       
import serial
import struct
import time


data = serial.Serial('/dev/ttyACM0', 115200)

def checkHumidity():
    i = "h".encode() #Arduino is ascii, python is unicode
    data.write(i)
    while True:
        if (data.in_waiting > 0):
            result = data.readline()
            humiVal = float(result.strip().decode("utf-8"))
#            print('Humidity:', humiVal)
            return humiVal
        time.sleep(0.01)
        
def checkTemperature():
    i = "t".encode() #Arduino is ascii, python is unicode
    data.write(i)
    while True:
        if (data.in_waiting > 0):
            result = data.readline()
            tempVal = float(result.strip().decode("utf-8"))
#            print('Temperature:', tempVal)
            return tempVal
        time.sleep(0.01)




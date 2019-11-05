import RPi.GPIO as GPIO
from time import sleep

plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

waterTypes = { "xeric" : [20,29] ,
               "mesic" : [30,49] ,
               "hydric" : [50,60] 
                }

def WaterControl(command, humVal=0, minHum=0):
    
#     print('Value:', min(waterTypes[plantDict["plantA"]["waterType"]]))
    if command: 
        if humVal < minHum:
    #         print("humidity ==> ",humVal)
            return WaterPump(2) # 5 sec is time for openning valve

def WaterPump(seconds):
    
    GPIO.setmode(GPIO.BCM)
    pump_relay = 26
    GPIO.setwarnings(False)
    GPIO.setup(pump_relay, GPIO.OUT)

#     GPIO.output(pump_relay, 1)
#     sleep(1)
#     try:
    GPIO.output(pump_relay, 0)
    GPIO.output(pump_relay, 1)
    
    return True
#     print("I pump for", seconds , "secs!")
#     except KeyboardInterrupt:
#          print("I except na")
    


import RPi.GPIO as GPIO
from time import sleep

plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

waterTypes = { "xeric" : 20 ,
               "mesic" : 30 ,
               "hydric" : 50 
                }

def WaterControl(humVal):   
    if humVal < waterTypes[plantDict["plantA"]["waterType"]]:
        print("humidity ==> ",humVal)
        WaterPump(3) # 3 sec is time for openning valve
    
def WaterPump(seconds):
    GPIO.setmode(GPIO.BCM)
    pump_relay = 26
    GPIO.setup(pump_relay, GPIO.OUT)
    GPIO.output(pump_relay, 1)
    
#     try:
    GPIO.output(pump_relay, 0)
    sleep(seconds)
    GPIO.output(pump_relay, 1)
    print("I pump for", seconds , "secs!")
        
#     except KeyboardInterrupt:
#          print("I except na")
    GPIO.cleanup()
    GPIO.setwarnings(False)
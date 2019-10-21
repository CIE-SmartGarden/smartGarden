import RPi.GPIO as GPIO
from time import sleep

def HeatControl(tempVal):
    
    plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

    tempTypes = {  "tropical" : 26 ,
               "temperate": 19 ,
                }
    if tempVal > tempTypes[plantDict['plantA']['tempType']]:
        print("Fan OPEN!!!")
        FanBlow(8)
    else:
        # Heat up
        print("Fan CLOSE!!!")
    
def FanBlow(seconds):
    
    GPIO.setmode(GPIO.BCM)
    fan_relay = 25
    GPIO.setup(fan_relay, GPIO.OUT)
    
    GPIO.output(fan_relay, 0)
    sleep(seconds)
    GPIO.output(fan_relay, 1)
    
    GPIO.cleanup()
    GPIO.setwarnings(False)
    print("OK")


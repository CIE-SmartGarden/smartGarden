import RPi.GPIO as GPIO
from time import sleep

def HeatControl(tempVal):
    
    plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

    tempTypes = {  "tropical" : [25,40] ,
               "temperate": [15,24] 
                }   # temperate = 15-25 ==> mean 20 , tropical = 25-40 ==> mean 32.5
    
    if tempVal > max(tempTypes[plantDict['plantA']['tempType']]): # too hot # 15 min 25 max
#         print("Fan OPEN!!!")
        return FanBlow(True)
    elif tempVal < min(tempTypes[plantDict['plantA']['tempType']]):
#         print("Fan CLOSE!!!")
        FanBlow(False)
        pass # Heat up # Fan Close
    else:
        # Temp OK!!! ==> stop heating , fan close
#         print("Fan CLOSE!!!")
        return FanBlow(False)
        
        
    
def FanBlow(command):
    GPIO.setmode(GPIO.BCM)
    fan_relay = 25
    GPIO.setwarnings(False)
    GPIO.setup(fan_relay, GPIO.OUT)
    if command:
        GPIO.output(fan_relay, 0)
    else:
        GPIO.output(fan_relay, 1)



import RPi.GPIO as GPIO
from time import sleep

async def HeatControl(tempVal, maxTemp, minTemp):
    
    plantDict = { "water spinach": {"tempType" : 'tropical', "waterType" : 'hydric'},
              "plantA": {"tempType" : 'temperate', "waterType": 'mesic'}
                }

    tempTypes = {  "tropical" : [25,40] ,
               "temperate": [15,24] 
                }   # temperate = 15-25 ==> mean 20 , tropical = 25-40 ==> mean 32.5
    if tempVal > maxTemp: # too hot # 15 min 25 max
#         print("Fan OPEN!!!")
        return await FanBlow(True)
    elif tempVal < minTemp:
#         print("Fan CLOSE!!!")
        await FanBlow(False)
        pass # Heat up # Fan Close
        return
    else:
        # Temp OK!!! ==> stop heating , fan close
#         print("Fan CLOSE!!!")
        return await FanBlow(False)
        
        
    
async def FanBlow(command):
    GPIO.setmode(GPIO.BCM)
    fan_relay = 25
    GPIO.setwarnings(False)
    GPIO.setup(fan_relay, GPIO.OUT)
    if command:
        GPIO.output(fan_relay, 0)
        return True
    else:
        GPIO.output(fan_relay, 1)
        return False



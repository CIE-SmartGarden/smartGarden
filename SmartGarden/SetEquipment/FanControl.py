import RPi.GPIO as GPIO
from time import sleep

def HeatControl(tempVal, maxTemp, minTemp):
    
    if tempVal > maxTemp: # too hot # 15 min 25 max
#         print("Fan OPEN!!!")
        return FanBlow(True)
    elif tempVal < minTemp:
#         print("Fan CLOSE!!!")
        FanBlow(False)
        pass # Heat up # Fan Close
        return
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
        return True
    else:
        GPIO.output(fan_relay, 1)
        return False



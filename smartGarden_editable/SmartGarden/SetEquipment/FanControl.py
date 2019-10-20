import RPi.GPIO as GPIO
from time import sleep

def HeatControl(tempVal):
    Kaprao ={
        'temp':24 ,
        'light_sec':12 ,
        'humidity':45 ,
        'soil_moist':60 ,
                }
    if tempVal < Kaprao['temp']:
        FanBlow(x)  # need to find heat rate per sec 
    
def FanBlow(seconds):
    
    while True:
        GPIO.setmode(GPIO.BCM)
        pump_relay = 24
        GPIO.setup(fan_relay, GPIO.OUT)
        GPIO.output(fan_relay, 1)
        try:
            GPIO.output(fan_relay, 0)
            sleep(seconds)
            
            GPIO.output(fan_relay, 1)
            sleep(1)
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()
    GPIO.setwarnings(False)


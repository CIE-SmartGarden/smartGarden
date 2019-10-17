import RPi.GPIO as GPIO
from time import sleep

def WaterControl(humVal):
    if humVal > 50:
        WaterPump(sec) #second for watering plant
    
def WaterPump(seconds):
    while True:
        GPIO.setmode(GPIO.BCM)
        pump_relay = 26
        GPIO.setup(pump_relay, GPIO.OUT)
        GPIO.output(pump_relay, 1)
        try:
            GPIO.output(pump_relay, 0)
            sleep(seconds)
            GPIO.output(pump_relay, 1)
            sleep(1)
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()
    GPIO.setwarnings(False)


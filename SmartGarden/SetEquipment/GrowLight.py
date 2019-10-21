import RPi.GPIO as GPIO
from time import sleep

Kaprao = { "light_sec" : 12
             }

def A_LightControl():
    if 'light_sec' in Kaprao:
        time_p = ((Kaprao['light_sec'])*60*60)
        print(time_p)
        return time_p
    else:
        pass
    
def A_Light(sec):
    #print(sec)
    
    while True:
        GPIO.setmode(GPIO.BCM)
        light_relay = 23
        GPIO.setup(light_relay, GPIO.OUT)
        GPIO.output(light_relay, 1)
        try:
            GPIO.output(light_relay, 0)
            sleep(sec)
            GPIO.output(light_relay, 1)
            sleep(24*60*60 - sec)
            
        except KeyboardInterrupt:
            pass
        GPIO.cleanup()
    GPIO.setwarnings(False)
    
#A_Light(2)
A_Light(A_LightControl())
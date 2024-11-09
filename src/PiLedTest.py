import RPi.GPIO as GPIO
from time import sleep
from hal import hal_led as led  

SWITCH_PIN = 22  
BLINK_FREQUENCY = 5  
BLINK_INTERVAL = 1 / (BLINK_FREQUENCY * 2)  

def init():
    GPIO.setmode(GPIO.BCM) 
    GPIO.setwarnings(False)
    GPIO.setup(SWITCH_PIN, GPIO.IN)  
    led.init()  

def read_slide_switch():
    return GPIO.input(SWITCH_PIN)

def main():
    init()  
    
    try:
        while True:
            if read_slide_switch():  
                led.on()
                sleep(BLINK_INTERVAL)
                led.off()
                sleep(BLINK_INTERVAL)
            else: 
                led.off()
                sleep(0.1) 

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()



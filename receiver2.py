import sys
import RPi.GPIO as GPIO
import time

def get_gpio_value(b0, b1, b2, b3, b4, b5, b6, b7):
    return (
        GPIO.input(b7) << 7 |
        GPIO.input(b6) << 6 |
        GPIO.input(b5) << 5 |
        GPIO.input(b4) << 4 |
        GPIO.input(b3) << 3 |
        GPIO.input(b3) << 3 | 
        GPIO.input(b2) << 2 | 
        GPIO.input(b1) << 1 | 
        GPIO.input(b0)
    )


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 4
b0 = 17
b1 = 27
b2 = 22
b3 = 23
b4 = 14
b5 = 15
b6 = 18
b7 = 24

GPIO.setup(clk, GPIO.OUT)
GPIO.setup(b0, GPIO.IN)
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)
GPIO.setup(b4, GPIO.IN)
GPIO.setup(b5, GPIO.IN)
GPIO.setup(b6, GPIO.IN)
GPIO.setup(b7, GPIO.IN)

for n in range(100000):
    GPIO.output(clk, GPIO.HIGH)
    # print(get_gpio_value(b0, b1, b2, b3, b4, b5, b6, b7))
    time.sleep(0.0001)
    GPIO.output(clk, GPIO.LOW)
    print(get_gpio_value(b0, b1, b2, b3, b4, b5, b6, b7))
    time.sleep(0.0001)
    
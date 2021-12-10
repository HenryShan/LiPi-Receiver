import sys
import RPi.GPIO as GPIO
import time

def get_gpio_value(b0, b1, b2, b3):
    return (GPIO.input(b3) << 3 | GPIO.input(b2) << 2 | GPIO.input(b1) << 1 | GPIO.input(b0))


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 4
b0 = 17
b1 = 27
b2 = 22
b3 = 23

GPIO.setup(clk, GPIO.OUT)
GPIO.setup(b0, GPIO.IN)
GPIO.setup(b1, GPIO.IN)
GPIO.setup(b2, GPIO.IN)
GPIO.setup(b3, GPIO.IN)

for n in range(100000):
    GPIO.output(clk, GPIO.HIGH)
    print(get_gpio_value(b0, b1, b2, b3))
    time.sleep(0.2)
    GPIO.output(clk, GPIO.LOW)
    print(get_gpio_value(b0, b1, b2, b3))
    time.sleep(0.2)
    
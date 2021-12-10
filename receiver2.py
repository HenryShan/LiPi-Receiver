import sys
import RPi.GPIO as GPIO
import time


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
    print(b3 << 3 | b2 << 2 | b1 << 1 | b0)
    time.sleep(0.5)
    GPIO.output(clk, GPIO.LOW)
    print(b3 << 3 | b2 << 2 | b1 << 1 | b0)
    time.sleep(0.5)
    
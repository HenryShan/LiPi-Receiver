import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 5
GPIO.setup(clk, GPIO.OUT)

for n in range(100000):
    GPIO.output(clk, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(clk, GPIO.LOW)
    time.sleep(0.001)
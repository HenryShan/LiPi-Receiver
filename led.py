import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 5
GPIO.setup(clk, GPIO.OUT)

while True:
    time.sleep(0.001 - (time.time_ns() / 1000**3) % 0.001)
    GPIO.output(clk, GPIO.HIGH)
    time.sleep(0.001 - (time.time_ns() / 1000**3) % 0.001)
    GPIO.output(clk, GPIO.LOW)
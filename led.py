import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 13
GPIO.setup(clk, GPIO.OUT)
period = 1000000

while True:
    time.sleep((period - time.time_ns() % period) / 1000000000)
    GPIO.output(clk, GPIO.HIGH)
    time.sleep((period - time.time_ns() % period) / 1000000000)
    GPIO.output(clk, GPIO.LOW)
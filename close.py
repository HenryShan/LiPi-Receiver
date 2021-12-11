import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clk = 13
GPIO.setup(clk, GPIO.OUT)
GPIO.output(clk, GPIO.LOW)
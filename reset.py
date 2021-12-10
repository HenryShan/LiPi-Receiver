import RPi.GPIO as GPIO


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

GPIO.cleanup()
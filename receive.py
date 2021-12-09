from gpiozero import SmoothedInputDevice
from time import sleep

light_sensor = SmoothedInputDevice(18)

while True:
    print(light_sensor.value)
    sleep(0.1)

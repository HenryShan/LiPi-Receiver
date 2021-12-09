from gpiozero import LightSensor
from time import sleep

light_sensor = LightSensor(18)

while True:
    print(light_sensor.value)
    sleep(0.1)

import sys
import RPi.GPIO as GPIO
import time
from encode import encode4b5b


bits_num = 16
header = "11000"
terminate = "0010000100"
end = "01101"
period = 2000000

def led_control(bits_list):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, GPIO.LOW)
    for bit in bits_list:
        time.sleep((period - time.time_ns() % period) / 1000000000)
        if bit == '1':
            GPIO.output(13, GPIO.HIGH)
        else:
            GPIO.output(13, GPIO.LOW)
    
    time.sleep((period - time.time_ns() % period) / 1000000000)
    GPIO.output(13, GPIO.LOW)
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Should input file name')
        sys.exit(1)
    path = "./" + sys.argv[1]
    data_bits = header + encode4b5b(path) + end
    print(data_bits)
    print(len(data_bits))
    while True:
        led_control(data_bits)
        time.sleep(0.5)


    # while True:
    #     n = 0
    #     pkt = ""
    #     while n < len(data_bits):
    #         # 32 bit / pkt
    #         if n + bits_num >= len(data_bits):
    #             pkt = header + data_bits[n:len(data_bits)]
    #             print(pkt[5:])
    #             led_control(pkt)
    #             # time.sleep(0.25)
    #             led_control(header + terminate)
    #             print(terminate)
    #             break
    #         else:
    #             pkt = header + data_bits[n:n+bits_num]
    #             print(pkt[5:])
    #             led_control(pkt)
    #             # time.sleep(0.25)
    #         n += bits_num
    #     # time.sleep(1)

from adc0820 import ADC0820
import time

period = 1000000
ns_in_s = 1000000000

receiver = ADC0820(
    db0=17, db1=27, db2=22, db3=23,
    db4=24, db5=25, db6=5, db7=6,
    rd_n=18, int_n=19, cs_n=20, ofl_n=21,
    wr_n=16, mode=26
)

while True:
    delta = (period - time.time_ns() % period) / ns_in_s
    time.sleep(0.001 - (time.time_ns() / 1000**3) % 0.001)
    print(receiver.read())

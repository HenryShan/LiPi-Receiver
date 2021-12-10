from adc0820 import ADC0820

receiver = ADC0820(
    db0=17, db1=27, db2=22, db3=23,
    db4=24, db5=25, db6=5, db7=6,
    rd_n=18, int_n=19, cs_n=20, ofl_n=21,
    wr_n=16, mode=26
)

while True:
    print(receiver.read())

import sys
import binascii

def encode(argv):
    text = argv
    if len(text) >= 64 :
        print('input length goes over the higher bond')
        sys.exit(0)        
    text_bytes = bytearray(text, 'utf-8')
    text_bits = []
    manchester_bits = []
    for byte in text_bytes:
        bits = bin(byte).replace('0b','')
        while len(bits) < 8:
            bits = '0' + bits
        text_bits += list(bits)
        for bit in list(bits.replace('0b', '')):
            if bit == '1':
                manchester_bits.append('1')
                manchester_bits.append('0')
            elif bit == '0':
                manchester_bits.append('0')
                manchester_bits.append('1')
    result = str(manchester_bits)
    return result, len(text)

def encode4b5b(file_path):
    with open(file_path, mode="rb") as file:
        file_bits = file.read()
    hex_str = str(binascii.hexlify(file_bits))[2:-1]
    print(hex_str)
    encode_dict = {
        "0":"11110",
        "1":"01001",
        "2":"10100",
        "3":"10101",
        "4":"01010",
        "5":"01011",
        "6":"01110",
        "7":"01111",
        "8":"10010",
        "9":"10011",
        "a":"10110",
        "b":"10111",
        "c":"11010",
        "d":"11011",
        "e":"11100",
        "f":"11101"
    }
    #calibration bits
    bits = ""
    for char in hex_str:
        bits += encode_dict[char]
    return bits


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.stderr.write('Should input at least one argument')
        sys.exit(1)
    encode(sys.argv[1])

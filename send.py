from transmit import transmit
import sys

period = 5000000

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Should input file name')
        sys.exit(1)
    filename = sys.argv[1]
    transmit(filename, period)
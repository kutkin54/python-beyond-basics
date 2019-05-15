import bz2
import sys

opener = bz2.open

if __name__ == '__main__':
    print(sys.argv[1])
    print(' '.join(sys.argv[2:]))
    f = bz2.open(sys.argv[1], mode='wt')
    f.write(''.join(sys.argv[2:]))
    f.close()
from file_processor import file_processor
from compress import *

def main():
    file = './data/16x16zero.txt'
    f = file_processor(file)
    f.compress_file()
    print(f.size())
    print(f.size(f'{file}.utf8bin.re'))

if  __name__ == "__main__":
    main()
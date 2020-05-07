from file_processor import file_processor
from compress import *
import os

def main():
    directory = './data'

    # Delete all previous outputs and logs
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith('txt'):
                os.remove(os.path.join(root, file))
    # Compress all Files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                fp = file_processor(file.split('.')[0],
                    os.path.join(root, file),
                    os.path.join(directory, 'output'),
                    os.path.join(directory, 'log'),
                    os.path.join(directory, 'log.csv'))
                fp.compress_file()

if  __name__ == "__main__":
    main()
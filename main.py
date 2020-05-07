from file_processor import file_processor
from compress import *
import os

def main():
    directory = './data'

    # Delete trash
    for file in os.listdir(directory):
        if not file.endswith('.txt'):
            os.remove(os.path.join(directory, file))

    # Compress all Files
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            fp = file_processor(os.path.join(directory, file), os.path.join(directory, 'log'))
            fp.compress_file()

if  __name__ == "__main__":
    main()
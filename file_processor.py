import os
import compress

class file_processor():
    def __init__(self, file):
        self.__path = file
        # convert text to readable utf8 binary
        self.__path_bin = f'{self.__path}.utf8bin'
        self.text_to_bin()
    def get_path(self):
        return self.__path
    def size(self, file=None):
        # return number of bits in binary file
        return os.path.getsize(self.__path_bin) if file == None else os.path.getsize(file)
    def compress_file(self):
        # run length compression
        encoded = compress.encode_run_length(self.__path_bin)
        with open(f'{self.__path_bin}.re', 'w') as f:
            f.write(encoded)
    def text_to_bin(self):
        with open(self.__path, 'r') as f:
            txt_bin = ''
            for line in f:
                txt_bin += f"{''.join([bin(ord(char))[2:].zfill(8) for char in line])}"
        with open(self.__path_bin, 'w') as f:
            f.write(txt_bin)

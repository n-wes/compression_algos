import os
import compress
import pickle

# file extensions
utf = '.utf8bin'
re = '.re'
he =  '.huff'
pkl = '.pkl'

class file_processor():
    def __init__(self, file, log):
        self.__path = file
        self.__log = log
        # convert text to readable utf8 binary
        bin_str = self.text_to_bin(self.__path)
        save_string(self.__path, utf, bin_str)
        self.append_log(os.path.splitext(self.__path)[0].split('/')[-1])
        self.append_log('Original', len(bin_str))
    def get_path(self):
        return self.__path
    def size(self, file=None):
        # return number of bits in utf 8 binary
        return os.path.getsize(f'{self.__path}{utf}') if file == None else os.path.getsize(file)
    def compress_file(self):
        # run length compression
        rl_str = compress.encode_run_length(self.__path)
        save_string(self.__path, re, rl_str)
        rl_bin_str = self.text_to_bin(f'{os.path.splitext(self.__path)[0]}{re}')
        save_string(self.__path, [re,utf], rl_bin_str)
        self.append_log('Run-Length', len(rl_bin_str))
        # huffman compression
        huff_code = compress.build_code(self.__path)
        huff_str = compress.encode_huffman(self.__path, huff_code)
        save_string(self.__path, he, huff_str)
        save_object(self.__path, huff_code)
        self.append_log('Huffman', len(huff_str))
        self.append_log()
    def text_to_bin(self, file):
        with open(file, 'r') as f:
            txt_bin = ''
            for line in f:
                txt_bin += f"{''.join([bin(ord(char))[2:].zfill(8) for char in line])}"
        return txt_bin
    def append_log(self, file=None, size=None):
        with open(self.__log, 'a') as f:
            if file == None:
                f.write('\n')
            elif size == None:
                f.write(f'{file}\n')
            else:
                f.write(f'{file}: {size} bits\n')

# save data
def save_string(path, endings, str):
    ending = ''.join(endings)
    with open(f'{os.path.splitext(path)[0]}{ending}', 'w') as f:
        f.write(str)
def save_object(path, obj):
    with open(f'{os.path.splitext(path)[0]}{pkl}', 'wb') as f:
        pickle.dump(obj, f)
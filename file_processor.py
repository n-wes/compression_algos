import os
import compress
import pickle

# file extensions
utf = '.utf8bin'
re = '.re'
he =  '.huff'
pkl = '.pkl'

class file_processor():
    def __init__(self, filename, input_path, output_path, log_path, log_csv_path):
        self.__filename = filename
        self.__input_path = input_path
        self.__output_path = output_path
        self.__log = log_path
        self.__log_csv = log_csv_path
        # convert text to readable utf8 binary
        bin_str = self.text_to_bin(self.__input_path)
        self.save_string(utf, bin_str)
        self.append_log(self.__filename)
        self.append_log('Original', len(bin_str))
        self.append_log_csv(self.__filename)
        self.append_log_csv(len(bin_str))
    def get_path(self):
        return self.__input_path
    def size(self, file=None):
        # return number of bits in utf 8 binary
        return os.path.getsize(f'{self.__input_path}{utf}') if file == None else os.path.getsize(file)
    def compress_file(self):
        # run length compression
        rl_str = compress.encode_run_length(self.__input_path)
        self.save_string(re, rl_str)
        rl_bin_str = self.text_to_bin(os.path.join(self.__output_path, self.__filename + re))
        self.save_string([re,utf], rl_bin_str)
        self.append_log('Run-Length', len(rl_bin_str))
        self.append_log_csv(len(rl_bin_str))
        # huffman compression
        huff_code = compress.build_code(self.__input_path)
        huff_str = compress.encode_huffman(self.__input_path, huff_code)
        self.save_string(he, huff_str)
        self.save_object(huff_code)
        self.append_log('Huffman', len(huff_str))
        self.append_log_csv(len(huff_str))
        self.append_log()
    def text_to_bin(self, file):
        with open(file, 'r') as f:
            txt_bin = ''
            for line in f:
                txt_bin += f"{''.join([bin(ord(char))[2:].zfill(8) for char in line])}"
        return txt_bin
    # Save Data
    def append_log(self, data=None, size=None):
        # Update log
        with open(self.__log, 'a') as f:
            if data == None:
                f.write('\n')
            elif size == None:
                f.write(f'{data}\n')
            else:
                f.write(f'{data}: {size} bits\n')
    def append_log_csv(self, data):
        with open(self.__log_csv, 'a') as f:
            if os.stat(self.__log_csv).st_size == 0:
                f.write('file_name, original_size, run_length_size, huffman_size')
            if type(data) != int:
                f.write(f'\n{data}')
            else:
                f.write(f',{data}')
            
    def save_string(self, endings, str):
        ending = ''.join(endings)
        with open(os.path.join(self.__output_path, self.__filename + ending), 'w') as f:
            f.write(str)
    def save_object(self, obj):
        with open(os.path.join(self.__output_path, self.__filename + pkl), 'wb') as f:
            pickle.dump(obj, f)
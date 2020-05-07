from itertools import *

def encode_run_length(file):
    encoded_string = ''
    with open(file, 'r') as f:
        bin_to_char = {'0':'a', '1':'b'}
        for line in f:
            for char, group in groupby(line):
                encoded_string += f'{len(list(group))}{bin_to_char[char]}'
    return encoded_string

def decode_run_length(file):
    decoded_string = ''
    with open(file, 'r') as f:
        for line in f:
            char_to_print = False
            count = 0
            for char in line:
                if not char.isdigit():
                    char_to_print = True
                if char == '/':
                    char_to_print = True
                    continue
                if char_to_print:
                    decoded_string += char * count
                    count = 0
                    char_to_print = False
                else:
                    count = count*10+ int(char)
    return decoded_string



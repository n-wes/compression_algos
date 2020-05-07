from itertools import *
import heapq

# Run-length Encoding

def encode_run_length(file):
    encoded_string = ''
    with open(file, 'r') as f:
        for line in f:
            for char, group in groupby(line):
                encoded_string += f'{len(list(group))}{char}'
    return encoded_string

# Huffman Encoding
# http://www.openbookproject.net/py4fun/huffman/huffman.html used as reference

def frequency(file):
    frequencies = dict()
    # count occurence of each character in file
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                frequencies[char] = frequencies.get(char,0) + 1
    return frequencies

def sort_frequencies(frequencies):
    keys = frequencies.keys()
    pairs = []
    for k in keys:
        pairs.append((frequencies[k], k))
    pairs.sort()
    return pairs

# build tree of key,frequency pairs
def build_tree(pairs):
    while(len(pairs) > 1):
        smallest_pair = tuple(pairs[0:2])
        rest = pairs[2:]
        comb = smallest_pair[0][0] + smallest_pair[1][0]
        pairs = rest + [(comb, smallest_pair)]
        pairs.sort(key=lambda t: t[0])
    return pairs[0]

# erases frequency counts from the tree
def trim_tree(tree):
    p = tree[1]
    return p if type(p) == type('') else (trim_tree(p[0]), trim_tree(p[1]))

def assign_codes(codes, char, pat=''):
    if type(char) == type(''):
        codes[char] = pat
    else:
        assign_codes(codes, char[0], pat + '0') # add 0 for left traversal
        assign_codes(codes, char[1], pat + '1') # add 1 for right traversal

def build_code(file):
    huff_code = dict()
    frequencies = frequency(file)
    pairs = sort_frequencies(frequencies)
    huff_tree = build_tree(pairs)
    trimmed_tree = trim_tree(huff_tree)
    assign_codes(huff_code, trimmed_tree)
    return huff_code

def encode_huffman(file, code):
    encoded_string = ''
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                encoded_string += code[char]
    return encoded_string
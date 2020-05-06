from file_processor import file_processor

def main():
    f = file_processor('./data/')
    print(f.size('ex_1.txt'))
    f.compress_file('ex_1.txt')

if  __name__ == "__main__":
    main()
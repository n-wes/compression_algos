import os
import compress

class file_processor():
    def __init__(self, folder_path):
        self.__path = folder_path
    def get_path(self):
        return self.__path
    def size(self, file):
        return os.path.getsize(f'{self.__path}/{file}')
    def compress_file(self, file):
        compress.run_length(f'{self.__path}/{file}')



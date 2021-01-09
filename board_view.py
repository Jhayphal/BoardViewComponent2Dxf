from os import path
from fz_file import FzFile
from bdv_file import BdvFile


class BoardView:
    def __init__(self, object_name, file_name):
        self.object_name = object_name
        self.file_name = file_name

        self.initialized = False
        self.points = []

    @staticmethod
    def createInstance(object_name, file_name):
        extension = path.splitext(file_name)[1].lower()

        if extension == '.bdv':
            return BdvFile(object_name, file_name)

        elif extension == '.fz':
            return FzFile(object_name, file_name)

        else:
            print('Указан файл неизвестного формата.')

            return BoardView(object_name, file_name)


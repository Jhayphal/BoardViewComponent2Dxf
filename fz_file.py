import RC6
import zlib

from board_view import BoardView


class FzFile(BoardView):
    def __init__(self, object_name, file_name):
        super(FzFile, self).__init__(object_name, file_name)

        key = bytes([0 for i in range(44)])

        self.initialized = False
        self.points = []

        with open(file_name, 'rb') as raw_data:
            start = raw_data.read(6)

            if not (start[4] == 0x78 and (start[5] == 0x9C or start[5] == 0xDA)):
                raw_data.seek(0, 0)

                data = self.decrypt(raw_data.read(), key)

            else:
                data = raw_data.read()

            with open('D:\\en_test.txt', 'wb') as dst:
                dst.write(data)

            content, content_size, description, description_size = FzFile.split(data)

            if content is None:
                return

            content = str(zlib.decompress(content, content_size))

            for i in content.splitlines():
                print(i)

            description = str(zlib.decompress(description, description_size).decode('utf-8'))

            for i in description.splitlines():
                print(i)

    @staticmethod
    def split(data):
        count = len(data)
        length = (data[count - 1] << 24) + (data[count - 2] << 16) + (data[count - 3] << 8) + data[count - 4]

        print(length, count)

        if length < 0 or length > count:
            print('Ошибка чтения размеров блоков: файл поврежден.')

            return None, None, None, None

        content = data[4:]
        content_size = count - length + 4

        description = data[content_size:]
        description_size = length

        return content, content_size, description, description_size

    @staticmethod
    def decrypt(data, key):
        cipher = RC6.Coder()
        encoding = 'cp866'
        bin_massage = cipher.bytesToBin(data.decode(encoding).encode('utf-8'))
        bin_key = cipher.bytesToBin(key.decode(encoding).encode('utf-8'))

        return cipher.binToBytes(cipher.decription(bin_massage, bin_key, w=32, r=20))
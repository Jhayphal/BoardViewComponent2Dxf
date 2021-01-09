import re

from os import path
from board_view import BoardView


class BdvFile(BoardView):
    def __init__(self, object_name, file_name):
        super(BdvFile, self).__init__(object_name, file_name)

        data = BdvFile.decode(file_name)

        if data == '':
            return

        print('Поиск объекта...')

        in_process = False

        data = data.splitlines()
        search_expression = re.compile(r'^Part\s+' + object_name, re.IGNORECASE)

        for line in data:
            line = line.rstrip()

            if in_process:
                if line == '':
                    continue

                if line.startswith('Part'):
                    break

                columns = line.split()

                x = float(columns[2]) * 1000.0
                y = float(columns[3]) * 1000.0

                self.points.append([x, y])

            elif search_expression.match(line) is not None:
                in_process = True

                print('Объект найден.')
                print('Загрузка объекта...')

        self.initialized = in_process

        if in_process:
            print('Объект загружен.')
        else:
            print('Указанный объект не найден.')

    @staticmethod
    def decode(file_name):
        print('Дешифровка данных...')

        result = b''

        with open(file_name, 'rb') as scheme:
            raw_text = scheme.readlines()
            count = 0xA0

            for line in raw_text:
                i = 0
                l = len(line)

                while i < l:
                    c = line[i]

                    if c == ord('\r') and line[i + 1] == ord('\n'):
                        count += 1

                    elif c != ord('\n'):
                        c = count - c

                    if count > 285:
                        count = 159

                    result += c.to_bytes(1, byteorder="little", signed=False)

                    i += 1

        file_name_parts = path.splitext(file_name)
        output_file_name = file_name_parts[0] + '_decrypted' + file_name_parts[1]

        with open(output_file_name, 'wb') as dst:
            dst.write(result)

        print('Данные расшифрованы.')

        return result.decode(encoding='utf-8')
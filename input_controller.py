from os import path


_error_num = 'Значение должно быть числом. Возможно, ошибка в разделителе (вместо точки запятая или наоборот).'


class InputController:
    @staticmethod
    def getFileName():
        while True:
            result = input('Имя файла (формата BDV): ').strip()

            if result == '':
                print('Значение не может быть пустым.')

            elif path.splitext(result)[1].lower() != '.bdv':
                print('Указан файл неизвестного формата. Поддерживается только формат BDV.')

            elif not path.exists(result):
                print('Файл не найден. Исправьте и попробуйте снова.')

            else:
                break

        return result

    @staticmethod
    def getObjectName():
        while True:
            result = input('Позиционный номер объекта: ').strip()

            if result == '':
                print('Значение не может быть пустым.')

            else:
                break

        return result.upper()

    @staticmethod
    def getFullWidth():
        while True:
            result = input('Ширина подложки, мм: ')

            try:
                result = float(result)

            except:
                print(_error_num)

            else:
                if result < 1.0:
                    print('Значение недопустимо.')

                else:
                    break

        return result

    @staticmethod
    def getLengthBetweenSidePins(full_width):
        while True:
            result = input('Растояние между крайними пинами: ')

            try:
                result = float(result)

            except:
                print(_error_num)

            else:
                if result < 1.0:
                    print('Значение недопустимо.')

                elif full_width is not None and result > float(full_width):
                    print('Значение не может превышать ширину подложки.')

                else:
                    break

        return result

    @staticmethod
    def getPinDiameter(length_between_side_pins):
        while True:
            result = input('Диаметр отверстия в трафарете: ')

            try:
                result = float(result)

            except:
                print(_error_num)

            else:
                if result <= 0.0:
                    print('Значение недопустимо.')

                elif length_between_side_pins is not None and result >= (float(length_between_side_pins) / 2):
                    print('Значение не может превышать половину растояния между пинами.')

                else:
                    break

        return result



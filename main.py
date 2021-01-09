from os import path
from board_view import BoardView
from dxf_designer import DxfDesigner
from input_controller import InputController

try:
    file_name = InputController.getFileName()
    object_name = InputController.getObjectName()

    file = BoardView.createInstance(object_name, file_name)

    if file.initialized:
        full_width = InputController.getFullWidth()
        length_between_side_pins = InputController.getLengthBetweenSidePins(full_width)
        pin_diameter = InputController.getPinDiameter(length_between_side_pins)

        designer = DxfDesigner(full_width, length_between_side_pins, pin_diameter)

        output_file_name = path.splitext(file_name)[0] + '.dxf'
        designer.draw(file.points, output_file_name)

except FileNotFoundError as e:
    print()
    print('Не хватает прав доступа для записи файла. Запустите программу от имени администратора или используйте DBV '
          'файлы в каталогах не требующих особых привилегий.')

except BaseException as e:
    print()
    print(str(e))

print()
input('Нажмите Enter для завершения...')


import ezdxf

from ezdxf import units


class DxfDesigner:
    def __init__(self, full_width, length_between_side_pins, pin_diameter):
        print('Вычисление параметров модели...')

        self.full_width = full_width
        self.length_between_side_pins = length_between_side_pins
        self.pin_diameter = pin_diameter

        self.margin = (full_width - length_between_side_pins) / 2
        self.pin_radius = pin_diameter / 2

        print('Параметры посчитаны.')

    def draw(self, points, file_name):
        count = len(points)

        if count == 0:
            print('Объект не содержит пинов.')

        else:
            print('Всего {} пинов.'.format(count))
            print('Рендеринг файла...')

            xAxis = [point[0] for point in points]
            yAxis = [point[1] for point in points]

            minX = min(xAxis)
            minY = min(yAxis)

            maxX = max(xAxis)
            maxY = max(yAxis)

            width = maxX - minX
            height = maxY - minY

            scale = self.length_between_side_pins / width
            full_height = (height * scale) + (self.margin * 2)

            rect = [
                (0, 0),
                (self.full_width, 0),
                (self.full_width, full_height),
                (0, full_height),
                (0, 0)
            ]

            leftShift = -minX
            rightShift = -minY

            doc = ezdxf.new()
            doc.units = units.MM
            space = doc.modelspace()

            space.add_lwpolyline(rect)

            for point in points:
                x = ((point[0] + leftShift) * scale) + self.margin
                y = ((point[1] + rightShift) * scale) + self.margin

                space.add_circle(center=(x, y), radius=self.pin_radius)

            doc.saveas(file_name)

            print('Готово.')

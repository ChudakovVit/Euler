from utils import *
from const import *


x = сonnectivity_components['x']
y = сonnectivity_components['y']


def get_field_from_number(number, x, y):
    """
    Возвращает массив массивов, заданных размеров из числа
    :param number: Число, которое нужно разбить
    :param x: размер стороны
    :param y: размер стороны
    :return: массив массивов нулей и единиц
    """
    # Перобразуем число к последовательности нулей и единиц
    bin_number = str(bin(number)[2:])
    bin_number = '0'*(x*y-len(bin_number)) + bin_number
    x_list = []
    for sub_x in range(x):
        y_list = []
        for sub_y in range(y):
            y_list.append(int(bin_number[0]))
            bin_number = bin_number[1:]
        x_list.append(y_list)
    return x_list


def generate_field(x, y):
    """
    Сгенерируем поле заданных размеров
    :param x: высота
    :param y: ширина
    :return:
    """
    for i in range(2**(x*y)):
        print(i)
        FIELD.set(get_field_from_number(i, x, y))
        FIELD.set_x_side_size(x+2)
        FIELD.set_y_side_size(y+2)
        file_output_field()

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


def generate_recursive_3_3(i, j):
    side_size = FIELD.get_side_size()
    for sub_i in range(i, side_size):
        FIELD.change_cell(sub_i, j)
        file_output_field()
        generate_recursive_3_3(sub_i + 1, j)
        for sub_j in range(j, side_size):
            FIELD.change_cell(sub_i, sub_j)
            file_output_field()
            generate_recursive_3_3(sub_i, sub_j+1)
    #
    # if i == FIELD.get_side_size():
    #     i = 0
    # else:
    #     FIELD.change_cell(i, j)
    #     print('#1 ' + str(i) + ' ' + str(j))
    #     file_output_field()
    #     generate_recursive_3_3(i+1, j)
    # if j == FIELD.get_side_size():
    #     return
    # else:
    #     FIELD.change_cell(i, j)
    #     print('#2 ' + str(i) + ' ' + str(j))
    #     file_output_field()
    #     generate_recursive_3_3(i, j+1)


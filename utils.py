from field import *
from const import *


def console_print_field():
    for i in range(len(FIELD.get())):
        field_str = ''
        for j in range(len(FIELD.get()[i])):
            field_str += str(FIELD.get()[i][j])
            field_str += ' '
        print(field_str)


def get_connectivity_count():
    extend_field = FIELD.add_edging()
    x = сonnectivity_components['x']
    y = сonnectivity_components['y']
    k_dict = {i: 0 for i in range(2**(x*y))}
    for i in range(FIELD.get_y_edging_size()-1):
        for j in range(FIELD.get_x_edging_size()-1):
            r_list = [i+r for r in range(y)]
            c_list = [j+c for c in range(x)]
            temp_list = [extend_field[r][c] for r in r_list for c in c_list]
            k_number = list(сonnectivity_components.keys())[list(сonnectivity_components.values()).index(temp_list)]
            k_dict[k_number] += 1
    return k_dict


def dict_beautifier(k_dict):
    dict_str = '\n'
    for key, value in k_dict.items():
        dict_str += 'K[{}] = {}'.format(key, value)
        dict_str += '\n'
    return dict_str


def get_zero_field(size, y_size=-1):
    """
    Генерирует нулевое поле заданного размера
    :param size: Размер поля без окаймления
    :return: массив массивов
    """
    if y_size == -1:
        y_size = size
    return [list(item) for item in [[0] * size] * y_size]


def get_field_info_string():
    """
    Получить информацию о поле и компонентах связности строкой для записи
    :return: str(dict)
    """

    strong_connectedly = FIELD.is_connectedly(type=0)
    waek_connectedly = FIELD.is_connectedly(type=1)

    if not any([strong_connectedly, waek_connectedly]):
        return 'not_connectedly'

    k_dict = get_connectivity_count()
    return str({
        'sc': str(strong_connectedly),  # strong connectedly
        'wc': str(waek_connectedly),  # weak connectedly
        's': str(k_dict[4] - k_dict[10] - k_dict[12]),  # strong
        'w': str(k_dict[4] + k_dict[9] - k_dict[12]),  # weak
        'f': str(FIELD.get()),  # field
        'c': str(k_dict)  # curve
    })


def get_field_info_eval(field_info):
    """
    Получить словарь со всей информацией о полях
    :param field_info:
    :return: dict
    """
    field_info = eval(field_info)
    for key, value in field_info.items():
        field_info[key] = eval(value)
    return field_info


"""--------------DEPRECATED--------------"""


def console_input_field():
    field = []
    for i in range(FIELD.side_size()):
        field.append([])
        for j in range(FIELD.side_size()):
            value = int(input('field[{i}][{j}] = '.format(i=i, j=j)))
            field[i].append(value)
    return field


def file_input_field():
    file = open('input.txt')
    field = []
    for line in file.readlines():
        sub_field = []
        for value in line:
            if not (value in (' ', '\n')):
                sub_field.append(int(value))
        field.append(sub_field)
    file.close()
    return field


def file_output_field(x='', y=''):
    """
    Записывает в файл полную информацию о поле
    :param x: размер поля в высоту (если есть)
    :param y: размер поля в ширину (если есть)
    """
    file_name = 'field_info{}.txt'.format('_'+(str(x)+'_'+str(y)) if x and y else '')
    file = open(file_name, 'a')  # w
    field_info = get_field_info_string()
    file.write(field_info + '\n')
    file.close()

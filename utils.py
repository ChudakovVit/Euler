import re
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

    # if not any([strong_connectedly, waek_connectedly]):
    #     return 'not_connectedly'

    k_dict = get_connectivity_count()
    return str({
        'br': str(FIELD.is_borders_reached()),  # is borders reached
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
    file_name = get_file_name(x, y)
    file = open(file_name, 'a')  # w
    field_info = get_field_info_string()
    file.write(field_info + '\n')
    file.close()


def get_from_file(x='', y='', number=0):
    """ Берем строку из файла
    """
    file_name = get_file_name(x, y)
    file_lines = open(file_name, 'r').readlines()

    return get_field_info_eval(file_lines.pop(number))


def get_file_name(x='', y=''):
    """ Хелпер для получения имени файла (для записи и чтения)
    """
    return 'field_info{}.txt'.format('_' + (str(x) + '_' + str(y)) if x and y else '')


def get_count_by_type(x='', y='', con_type=-1, borders_reached=None):
    """
    Считает в заданном файле количество изображений того или иного типа
    :param x: Размерность матрицы
    :param y: Размерность матрицы
    :param type: 0 - сильно связные, 1 - слабо, 2 - несвязные
    :return: Количество изобрабражений заданного типа в заданном файле
    """
    file_name = get_file_name(x, y)
    file_read = open(file_name, 'r').read()

    # br_pat = borders_reached if borders_reached is not None else r'.*?'
    # sc_pat = not bool(con_type) if con_type != -1 else r'.*?' if con_type is not None else False
    # wc_pat = bool(con_type) if con_type != -1 else r'.*?' if con_type is not None else False

    br_pat = borders_reached
    if borders_reached is None:
        br_pat = r'.*?'

    wc_pat = r'.*?'
    sc_pat = True
    if con_type is None:
        br_pat = r'.*?'
        sc_pat = wc_pat = False
    elif con_type == -1:
        sc_pat = wc_pat = r'.*?'
    elif con_type == 1:
        wc_pat = True
        sc_pat = r'.*?'

    pattern = r'''br': '{}', 'sc': '{}', 'wc': '{}'''.format(br_pat, sc_pat, wc_pat)

    find_in_file = re.findall(pattern, file_read)
    return len(find_in_file)


def get_all_counts():
    """ Выводит данные о всех типах для заданных размерностей
    """
    for x in range(1, 5):
        for y in range(1, 5):
            not_connectedly = get_count_by_type(x, y, None, None)

            con_type = 0
            strong_without = get_count_by_type(x, y, con_type, borders_reached=False)
            strong_with = get_count_by_type(x, y, con_type, borders_reached=True)
            strong_all = get_count_by_type(x, y, con_type, borders_reached=None)

            con_type = 1
            weak_without = get_count_by_type(x, y, con_type, borders_reached=False)
            weak_with = get_count_by_type(x, y, con_type, borders_reached=True)
            weak_all = get_count_by_type(x, y, con_type, borders_reached=None)

            all_items_count = get_count_by_type(x, y, -1, borders_reached=None)

            print('Несвязных: ', not_connectedly)

            print('Сильно связных без границы: ', strong_without)
            print('Сильно связных с границей: ', strong_with)
            print('Сильно связных всего: {} = {} + {}'.format(strong_all, strong_with, strong_without))

            print('Слабо связных без границы: ', weak_without)
            print('Слабо связных с границей: ', weak_with)
            print('Слабо связных всего: {} = {} + {}'.format(weak_all, weak_with, weak_without))

            print('Всего: {} = {} + {} + {}'.format(all_items_count, strong_all, weak_all, not_connectedly))
            print()


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

    strong_connectedly = FIELD.is_connectedly(type=1)
    waek_connectedly = FIELD.is_connectedly(type=0)

    if not any([strong_connectedly, waek_connectedly]):
        return None

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
    field_info = get_field_info_string()
    if field_info:
        file_name = get_file_name(x, y)
        file = open(file_name, 'a')  # w
        file.write(field_info + '\n')
        file.close()


def get_file_name(x='', y=''):
    """ Хелпер для получения имени файла (для записи и чтения)
    """
    return 'field_info{}.txt'.format('_' + (str(x) + '_' + str(y)) if x and y else '')


def get_count_by_type(con_type=0, borders_reached=None, file_name=None):
    """ Считает в заданном файле количество изображений того или иного типа
    """
    file_read = open(file_name, 'r').read()

    br_pat = borders_reached
    if borders_reached is None:
        br_pat = r'.*?'

    wc_pat = r'.*?' if con_type == 1 else True

    pattern = r'''br': '{}', 'sc': 'True', 'wc': '{}'''.format(br_pat, wc_pat)

    find_in_file = re.findall(pattern, file_read)
    return len(find_in_file)


def get_all_counts(x='', y='', files_list=None):
    """ Выводит данные о всех типах для заданных размерностей
    """

    strong_with = 0
    strong_all = 0

    weak_with = 0
    weak_all = 0

    if not files_list:
        files_list = [get_file_name(x, y)]

    for file_name in files_list:
        con_type = 1
        strong_with += get_count_by_type(con_type, borders_reached=True, full_file_name=file_name)
        strong_all += get_count_by_type(con_type, borders_reached=None, full_file_name=file_name)

        con_type = 0
        weak_with = get_count_by_type(con_type, borders_reached=True, full_file_name=file_name)
        weak_all = get_count_by_type(con_type, borders_reached=None, full_file_name=file_name)

    print('Для файлов ' + str(files_list))

    print('Сильно связных с границей: ', strong_with)
    print('Сильно связных всего: ', strong_all)

    print('Слабо связных с границей: ', weak_with)
    print('Слабо связных всего: ', weak_all)

    print()


def get_count_uniq_new(x='', y='', con_type=0, files_list=None):
    """ Выводит данные о различимых изображениях
    """

    all_dict = {}

    if not files_list:
        files_list = [get_file_name(x, y)]

    all_files_border_reached = 0

    for file_name in files_list:
        file_lines = open(file_name, 'r').readlines()

        border_reached = 0
        for line in file_lines:
            if not re.findall('''br': 'True''', line):
                continue
            line_con_type = 1
            if con_type == 0:
                if re.findall('''wc': 'True''', line):
                    line_con_type = 0

            if con_type != line_con_type:
                continue
            border_reached += 1

            k_dict = line[line.index(''', 'c''') + 7:]
            if k_dict in all_dict:
                all_dict[k_dict] += 1
            else:
                all_dict[k_dict] = 1

        all_files_border_reached += border_reached

    unic_count = 0
    max_value = 1
    for key, value in all_dict.items():
        if value == 1:
            unic_count += 1
        if value > max_value:
            max_value = value

    print('Тип связности: ' + str(con_type) +
          ' Количество уникальных: ' + str(unic_count) +
          ' Максимально встречается раз один и тот же набор: ' + str(max_value) +
          ' Всего типов наборов: ' + str(len(all_dict)) +
          ' Достигается граница: ' + str(all_files_border_reached)
    )

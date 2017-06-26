from const import *


def console_print_field():
    for i in range(len(FIELD.get())):
        field_str = ''
        for j in range(len(FIELD.get()[i])):
            field_str += str(FIELD.get()[i][j])
            field_str += ' '
        print(field_str)


def add_edging():
    ext_field = []
    for i in range(FIELD.get_N()):
        ext_field.append([])
        for j in range(FIELD.get_N()):
            val = 0 if i in (0, FIELD.get_N()-1) or j in (0, FIELD.get_N()-1) else FIELD.get()[i-1][j-1]
            ext_field[i].append(val)
    return ext_field


def get_connectivity_count():
    extend_field = add_edging()
    x = сonnectivity_components['x']
    y = сonnectivity_components['y']
    k_dict = {i: 0 for i in range(2**(x*y))}
    for i in range(FIELD.get_N()-1):
        for j in range(FIELD.get_N()-1):
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


def generate_field():
    x = сonnectivity_components['x']
    y = сonnectivity_components['y']
    for k in range(2**(x*y)):
        for i in range(0, len(FIELD.get()), 2):
            for j in range(0, len(FIELD.get()[i]), 2):
                for sub_i in range(i, len(FIELD.get()), 2):
                    for sub_j in range(j, len(FIELD.get()[i]), 2):
                        FIELD.set_cell(sub_i, sub_j, сonnectivity_components[k][0])
                        FIELD.set_cell(sub_i, sub_j+1, сonnectivity_components[k][1])
                        FIELD.set_cell(sub_i+1, sub_j, сonnectivity_components[k][2])
                        FIELD.set_cell(sub_i+1, sub_j+1, сonnectivity_components[k][3])
                        # print('i, j, k ', i, j, k, сonnectivity_components[k])
                        # print()
                        # file_output_field()
    FIELD.set(file_input_field())
    # TODO
    # file_output_field()


"""--------------DEPRECATED--------------"""


def add_log(func, arg, msg=''):
    pass
    # print('----------------------------------')
    # print(msg)
    # func(arg)
    # print('----------------------------------')


def console_input_field():
    field = []
    for i in range(FIELD.get_N()-2):
        field.append([])
        for j in range(FIELD.get_N()-2):
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


def file_output_field():
    file = open('db.txt', 'a')  # w
    for i in range(FIELD.get_N()-2):
        sub_line = ''
        for j in range(FIELD.get_N()-2):
            sub_line += str(FIELD.get()[i][j]) if FIELD.get() else str(0)
            sub_line += ' '
        sub_line += '\n'
        file.write(sub_line)
    file.write(str(get_connectivity_count())+'\n\n')
    file.close()

from view import *

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

def file_output_field(field):
    file = open('input.txt', 'w')
    for i in range(N-2):
        sub_line = ''
        for j in range(N-2):
            sub_line += str(field[i][j])
            sub_line += ' '
        sub_line += '\n'
        file.write(sub_line)
    file.close()

def console_input_field():
    field = []
    for i in range(N-2):
        field.append([])
        for j in range(N-2):
            value = int(input('field[{i}][{j}] = '.format(i=i, j=j)))
            field[i].append(value)

    return field

def console_print_field(field):
    field_str = ''
    for i in range(len(field)):
        field_str = ''
        for j in range(len(field[i])):
            field_str += str(field[i][j])
            field_str += ' '
        print(field_str)

def add_edging(field):
    new_field = []
    for i in range(N):
        new_field.append([])
        for j in range(N):
            if i in (0, N-1) or j in (0, N-1):
                new_field[i].append(0)
            else:
                new_field[i].append(field[i-1][j-1])
    return new_field

def get_conectivity_count(field):
    x = сonnectivity_components['x']
    y = сonnectivity_components['y']
    k_dict = {i: 0 for i in range(2**(x*y))}
    for i in range(N-1):
        for j in range(N-1):
            r_list = [i+r for r in range(y)]
            c_list = [j+c for c in range(x)]
            temp_list = [field[r][c] for r in r_list for c in c_list]
            k_number = list(сonnectivity_components.keys())[list(сonnectivity_components.values()).index(temp_list)]
            k_dict[k_number] += 1
    return k_dict

def dict_beautifier(k_dict):
    dict_str = '\n'
    for key, value in k_dict.items():
        dict_str += 'K_{} = {}'.format(key, value)
        dict_str += '\n'
    return dict_str


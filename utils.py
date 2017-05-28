from const import *

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

def get_conectivity_count(field, components=сonnectivity_components_2):
    n = components['n']
    k_dict = {i: 0 for i in range(2**n**2)}
    for i in range(N-1):
        for j in range(N-1):
            temp_list = [field[i][j], field[i][j + 1], field[i + 1][j], field[i + 1][j + 1]]
            k_number = list(components.keys())[list(components.values()).index(temp_list)]
            k_dict[k_number] += 1
    return k_dict


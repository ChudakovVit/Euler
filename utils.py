from const import *

сonnectivity_components = {
    0: [0, 0, 0, 0],
    1: [1, 0, 0, 0],
    2: [0, 1, 0, 0],
    3: [0, 0, 1, 0],
    4: [0, 0, 0, 1],
    5: [1, 0, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0],
    8: [0, 1, 0, 1],
    9: [1, 1, 0, 0],
    10: [0, 0, 1, 1],
    11: [1, 0, 1, 1],
    12: [1, 1, 0, 1],
    13: [1, 1, 1, 0],
    14: [0, 1, 1, 1],
    15: [1, 1, 1, 1],
    'n': 2
}

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
    for i in range(N-2):
        field_str = ''
        for j in range(N-2):
            field_str += str(field[i][j])
            field_str += ' '
        print(field_str)

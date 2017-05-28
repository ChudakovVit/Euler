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
    for i in range(N-2):
        field_str = ''
        for j in range(N-2):
            field_str += str(field[i][j])
            field_str += ' '
        print(field_str)

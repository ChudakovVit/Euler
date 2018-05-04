from field import *
from const import *


def generate_3_3():
    pass


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

    print(FIELD)
    # TODO
    # file_output_field()
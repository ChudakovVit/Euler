import view
from utils import *
from generate import *


def main():
    # x, y = 5, 7
    # z_field = get_zero_field(x, y)
    # FIELD.set(z_field)
    # FIELD.set_x_side_size(len(z_field[0])+2)
    # FIELD.set_y_side_size(len(z_field)+2)
    #
    # view.set_field()
    # view.mainloop()

    # get_from_file(1, 2, 3)

    with_type_0 = get_count_by_type(3, 3, 0)
    print(with_type_0)

    with_type_1 = get_count_by_type(3, 3, 1)
    print(with_type_1)


    with_type_2 = get_count_by_type(3, 3, 2)
    print(with_type_2)

    print('res :', with_type_1 + with_type_2)
    # generate_field(4, 5)
    # #
    # for i in range(3, 5):
    #     for j in range(3, 5):
    #         generate_field(i, j)
    #         if i != j:
    #             generate_field(j, i)



if __name__ == '__main__':
    main()

# 5x5 3483626
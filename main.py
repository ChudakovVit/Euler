import view
from utils import *
from generate import *


def main():
    x, y = 3, 5
    z_field = get_zero_field(x, y)
    FIELD.set(z_field)
    # FIELD.set_side_size(N)
    FIELD.set_x_side_size(len(z_field[0])+2)
    FIELD.set_y_side_size(len(z_field)+2)

    view.set_field()
    # file_output_field()

    # generate_field(5, 4)
    #
    # for i in range(1, 4):
    #     for j in range(1, 4):
    #         generate_field(i, j)
    #         if i != j:
    #             generate_field(j, i)

    view.mainloop()


if __name__ == '__main__':
    main()

# 5x5 3483626
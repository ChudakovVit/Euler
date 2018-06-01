import view
from utils import *
from generate import *


def main():
    FIELD.set(get_zero_field(N-2))
    FIELD.set_side_size(N)
    view.set_field()
    # file_output_field()

    # generate_field(5, 4)

    # for i in range(4, 5):
    #     for j in range(4, 5):
    #         generate_field(i, j)
    #         if i != j:
    #             generate_field(j, i)

    view.mainloop()


if __name__ == '__main__':
    main()

# 5x5 3483626
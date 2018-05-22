import view
from utils import *
from generate import *


def main():
    FIELD.set(get_zero_field(N-2))
    FIELD.set_side_size(N)
    # view.set_field()
    file_output_field()
    generate_recursive_3_3(0, 0)
    # generate_field()
    # view.mainloop()


if __name__ == '__main__':
    main()

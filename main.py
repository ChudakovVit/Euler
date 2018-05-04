import view
from field import *
from utils import *
from generate import *


def main():
    FIELD.set(file_input_field())
    FIELD.set_N(10)
    view.set_field()
    generate_3_3()
    # generate_field()
    view.mainloop()


if __name__ == '__main__':
    main()

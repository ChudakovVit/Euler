from view import *
from utils import *


def main():
    FIELD.set(file_input_field())
    FIELD.set_N(10)
    view_set_field()
    generate_field()
    mainloop()

if __name__ == '__main__':
    main()

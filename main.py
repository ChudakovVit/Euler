import test
from view import *
from utils import *

def main():
    field = file_input_field()
    console_print_field(field)
    print()
    new_field = add_edging(field)
    console_print_field(new_field)
    print()
    k_dict = get_conectivity_count(new_field, components=сonnectivity_components_2)
    print(k_dict)
    view_set_field(field)
    view_add_info(k_dict)
    mainloop()

if __name__ == '__main__':
    main()

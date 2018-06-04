def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Field:
    def __init__(self):
        self.field = []
        self.side_size = 0
        self.x_side_size = 0
        self.y_side_size = 0

    def get(self):
        """ Геттер для поля
        """
        return self.field

    def set(self, field):
        """ Сеттер для поля
        """
        self.field = field

    def change_cell(self, x, y):
        """ Изменить значение в ячейке на противоположное
        """
        change_field = self.field
        change_field[y][x] = 1 - change_field[y][x]
        self.set(change_field)

    def set_cell(self, x, y, color):
        """ Задать конкретной ячейке значение
        """
        self.field[y][x] = color

    def get_side_size(self):
        """ Получить размер поля с окаймлением
        """
        return self.side_size-2

    def get_x_side_size(self):
        """ Получить размер поля с окаймлением по высоте
        """
        return self.x_side_size-2

    def get_y_side_size(self):
        """ Получить размер поля с окаймлением по ширине
        """
        return self.y_side_size-2

    def set_side_size(self, side_size):
        """ Задать размер поля с окаймлением
        """
        self.side_size = side_size
        self.x_side_size = side_size
        self.y_side_size = side_size

    def set_x_side_size(self, side_size):
        """ Задать размер поля с окаймлением по высоте
        """
        self.x_side_size = side_size

    def set_y_side_size(self, side_size):
        """ Задать размер поля с окаймлением по ширине
        """
        self.y_side_size = side_size

    def get_edging_size(self):
        """ Получить размер поля с окаймлением
        """
        return self.side_size

    def get_x_edging_size(self):
        """ Получить размер поля с окаймлением по высоте
        """
        return self.x_side_size

    def get_y_edging_size(self):
        """ Получить размер поля с окаймлением по ширине
        """
        return self.y_side_size

    def add_edging(self):
        """
        Возвращает поле с окаймлением
        :return:
        """
        ext_field = []
        x_edging_size = FIELD.get_x_edging_size()
        y_edging_size = FIELD.get_y_edging_size()
        for i in range(y_edging_size):
            ext_field.append([])
            for j in range(x_edging_size):
                val = 0 if i in (0, y_edging_size - 1) or j in (0, x_edging_size - 1) else FIELD.get()[i - 1][j - 1]
                ext_field[i].append(val)
        return ext_field

    def is_connectedly(self, type=0):
        """
        Метод для определения связности поля
        :param type: тип связности: 0 - сильная, 1 - слабая
        :return: bool
        """

        def _get_first_fill(value=1):
            """ Возвращает первую закрашенную ячейку
            """
            for i in range(1, FIELD.get_y_edging_size() - 1):
                for j in range(1, FIELD.get_x_edging_size() - 1):
                    if field_copy[i][j] == value:
                        return i, j
            return -1, -1

        def _change_cells(x, y):
            """ Меняет на спецсимвол клетку и все ближлежайшие
            """
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # Условие на только нужные нам клетки
                    constraint = 0 in [i, j] if type == 0 else True
                    if constraint and field_copy[x+i][y+j] == 1:
                        field_copy[x+i][y+j] = -1
                        _change_cells(x+i, y+j)

        field_copy = list(list(item) for item in FIELD.add_edging())
        x, y = _get_first_fill()
        if x != -1:
            _change_cells(x, y)

        x, y = _get_first_fill()
        x_, y_ = _get_first_fill(value=-1)
        if x != -1 and x_ != -1:
            return False
        return True


FIELD = Field()

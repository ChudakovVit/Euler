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


FIELD = Field()

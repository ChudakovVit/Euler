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
        self.N = 0

    def get(self):
        return self.field

    def set(self, field):
        self.field = field

    def change_cell(self, x, y):
        change_field = self.field
        change_field[y][x] = 1 - change_field[y][x]
        self.set(change_field)

    def set_cell(self, x, y, color):
        self.field[y][x] = color

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N


FIELD = Field()

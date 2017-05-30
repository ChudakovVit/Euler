CELL_SIZE = 30  # размер ячейки
x0 = CELL_SIZE // 2  # отступ от левого края
y0 = CELL_SIZE // 2  # отступ от вернего края
COLORS = {0: 'white', 1: 'black'}  # выбор цвета для ячейки
N = 10  # размер с учетом окаймления

сonnectivity_components = {
    0: [0, 0, 0, 0],
    3: [1, 0, 0, 0],
    1: [0, 1, 0, 0],
    4: [0, 0, 1, 0],
    2: [0, 0, 0, 1],
    10: [1, 0, 0, 1],
    9: [0, 1, 1, 0],
    8: [1, 0, 1, 0],
    6: [0, 1, 0, 1],
    5: [1, 1, 0, 0],
    7: [0, 0, 1, 1],
    12: [1, 0, 1, 1],
    11: [1, 1, 0, 1],
    14: [1, 1, 1, 0],
    13: [0, 1, 1, 1],
    15: [1, 1, 1, 1],
    'x': 2, 'y': 2
}


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

    def get(self):
        return self.field

    def set(self, field):
        self.field = field

    def change_cell(self, x, y):
        change_field = self.field
        change_field[y][x] = 1 - change_field[y][x]
        self.set(change_field)

FIELD = Field()

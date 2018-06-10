import view
from tkinter import *
from utils import *

root = Tk()
root.title('Chudakov Vitaly')
root.geometry('660x330')
root.resizable(False, False)

canvas = Canvas(root, bg='grey')
canvas.pack(fill=BOTH, expand=1)


def add_cell(row, column, color):
    x1 = x0 + column * CELL_SIZE
    y1 = y0 + row * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS[color], outline=COLORS[1-color])


def set_field():
    x_edging_size = FIELD.get_x_edging_size()
    y_edging_size = FIELD.get_y_edging_size()
    for y in range(y_edging_size):
        for x in range(x_edging_size):
            val = 0 if y in (0, y_edging_size-1) or x in (0, x_edging_size-1) else FIELD.get()[y-1][x-1]
            view.add_cell(y, x, val)

    k_dict = get_connectivity_count()
    view.add_info(k_dict)


def add_info(k_dict):
    k_dict_label = Label(root, text=dict_beautifier(k_dict), bg='grey', justify=LEFT)
    k_dict_label.place(x=350, y=20)
    hi_1 = Label(root, text='Сильная связность: χ = {}    '.format(str(k_dict[4]-k_dict[10]-k_dict[12])), bg='grey',
                 justify=LEFT)
    hi_1.place(x=450, y=100)
    hi_2 = Label(root, text='Слабая связность: χ = {}    '.format(str(k_dict[4]+k_dict[9]-k_dict[12])), bg='grey',
                 justify=LEFT)
    hi_2.place(x=450, y=150)
    hi_3 = Label(root, text='Связно сильно: {}'.format(FIELD.is_connectedly(type=1)), bg='grey',
                 justify=LEFT)
    hi_3.place(x=450, y=200)
    hi_4 = Label(root, text='Связно слабо: {}'.format(FIELD.is_connectedly(type=0)), bg='grey',
                 justify=LEFT)
    hi_4.place(x=450, y=250)


def on_click(event):
    """
    Обработчик нажатия на клетку, для изменения цвета на противоположный
    """
    x = (event.x+x0)//CELL_SIZE - 2
    y = (event.y+y0)//CELL_SIZE - 2
    if not ((0 <= x < FIELD.get_x_side_size()) and (0 <= y < FIELD.get_y_side_size())):
        return
    update_field(x, y)


canvas.bind("<Button-1>", on_click)


def update_field(x, y):
    FIELD.change_cell(x, y)
    set_field()


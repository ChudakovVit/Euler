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
    edging_size = FIELD.get_edging_size()
    for i in range(edging_size):
        for j in range(edging_size):
            val = 0 if i in (0, edging_size-1) or j in (0, edging_size-1) else FIELD.get()[i-1][j-1]
            view.add_cell(i, j, val)

    k_dict = get_connectivity_count()
    print(FIELD.get())
    view.add_info(k_dict)


def add_info(k_dict):
    k_dict_label = Label(root, text=dict_beautifier(k_dict), bg='grey', justify=LEFT)
    k_dict_label.place(x=350, y=20)
    hi_1 = Label(root, text='Сильная связность: χ = {}    '.format(str(k_dict[4]-k_dict[10]-k_dict[12])), bg='grey', justify=LEFT)
    hi_1.place(x=450, y=100)
    hi_2 = Label(root, text='Слабая связность: χ = {}    '.format(str(k_dict[4]+k_dict[9]-k_dict[12])), bg='grey', justify=LEFT)
    hi_2.place(x=450, y=200)


def on_click(event):
    """
    Обработчик нажатия на клетку, для изменения цвета на противоположный
    """
    x = (event.x+x0)//CELL_SIZE - 2
    y = (event.y+y0)//CELL_SIZE - 2
    if not ((0 <= x < FIELD.get_side_size()) and (0 <= y < FIELD.get_side_size())):
        return
    update_field(x, y)


canvas.bind("<Button-1>", on_click)


def update_field(x, y):
    FIELD.change_cell(x, y)
    set_field()

    file_output_field()

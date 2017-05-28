from tkinter import *
from const import *
from utils import dict_beautifier

root = Tk()
root.title('Chudakov Vitaly IT-31')
root.geometry('660x330')
root.resizable(False, False)

canvas = Canvas(root, bg='grey')
canvas.pack(fill=BOTH, expand=1)

def view_add_cell(row, column, color):
    x1 = x0 + column * CELL_SIZE
    y1 = y0 + row * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS[color], outline=COLORS[1-color])

def view_set_field(field):
    for i in range(N):
        for j in range(N):
            if i in (0, N-1) or j in (0, N-1):
                view_add_cell(i, j, 0)
            else:
                view_add_cell(i, j, field[i-1][j-1])

def view_add_info(k_dict):
    k_dict_label = Label(root, text=dict_beautifier(k_dict), bg='grey', justify=LEFT)
    k_dict_label.place(x=350, y=20)

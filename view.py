from tkinter import *
from const import *
from utils import *
from main import *

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
    new_field = add_edging(field)
    k_dict = get_conectivity_count(new_field)
    view_add_info(k_dict)

def view_add_info(k_dict):
    k_dict_label = Label(root, text=dict_beautifier(k_dict), bg='grey', justify=LEFT)
    k_dict_label.place(x=350, y=20)

def view_on_click(event):
    x = (event.x+x0)//CELL_SIZE - 2
    y = (event.y+y0)//CELL_SIZE - 2
    if not ((0 <= x < N-2) and (0 <= y < N-2)):
        return
    update_field(x, y)
    print("clicked at", x, y)
canvas.bind("<Button-1>", view_on_click)

def update_field(x, y):
    # view_add_cell(y+1, x+1, 0)
    field = file_input_field()
    field[y][x] = 1-field[y][x]
    file_output_field(field)
    view_set_field(field)

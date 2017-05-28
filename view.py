from tkinter import *
from const import *

root = Tk()
root.title('Chudakov Vitaly IT-31')
root.geometry('660x330')

frame = Frame(root)
frame.pack()

canvas = Canvas(root, bg='grey')
canvas.pack(fill=BOTH, expand=1)

def add_cell(row, column, color):
    x1 = x0 + column * CELL_SIZE
    y1 = y0 + row * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS[color], outline=COLORS[1-color])

def set_field(field):
    for i in range(N):
        for j in range(N):
            if i in (0, N-1) or j in (0, N-1):
                add_cell(i, j, 0)
            else:
                add_cell(i, j, field[i-1][j-1])

import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox


FPS = 500   # 500
R = 20
C = 12
cell_size = 27  # 30
height = R*cell_size
width = C*cell_size
block_list = []
for i in range(R):
    i_row = ['' for j in range(C)]
    block_list.append(i_row)

SHAPES = {
    "O": [(-1, -1), (0, -1), (-1, 0), (0, 0)],
    "Z": [(-1, -1), (0, -1), (0, 0), (1, 0)],
    "S": [(-1, 0), (0, 0), (0, -1), (1, -1)],
    "T": [(-1, 0), (0, 0), (0, -1), (1, 0)],
    "I": [(0, 1), (0, 0), (0, -1), (0, -2)],
    "L": [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
    "J": [(-1, 0), (0, 0), (0, -1), (0, -2)]
}

# SHAPESCOLOR = {
#     "O": "blue",
#     "Z": "Cyan",
#     "S": "red",
#     "T": "yellow",
#     "I": "green",
#     "L": "purple",
#     "J": "orange"
# }

SHAPESCOLOR = {
    "O": "blue",
    "Z": "blue",
    "S": "blue",
    "T": "blue",
    "I": "blue",
    "L": "blue",
    "J": "blue"
}

def draw_cell_by_cr(canvas, c, r, color='#8888ff'):
    """
    canvas: 画板对象
    c: 方格所在列
    r: 方格所在行
    color: 方格颜色，默认值为'##8888ff'  青蓝色
    return:
    """
    x0 = c*cell_size
    y0 = r*cell_size

    x1 = c*cell_size + cell_size
    y1 = r*cell_size + cell_size
    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='#ccccff', width=2)  # 绘画

def save_to_block_list(block):
    shape_type = block['kind']
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc
        r = cell_r + cr

        block_list[r][c] = shape_type

def draw_board(canvas, block_list):
    for ri in range(R):
        for ci in range(C):
            cell_type = block_list[ri][ci]
            if cell_type:
                draw_cell_by_cr(canvas, ci, ri, SHAPESCOLOR[cell_type])
            else:
                draw_cell_by_cr(canvas, ci, ri)

def draw_cells(canvas, c, r, cell_list, color="#8888ff"):
    '''
    canvas: 画板对象
    c: 列
    r: 行
    cell_list: 各个点的坐标
    color: 颜色
    '''
    for cell in cell_list:
        cell_c, cell_r = cell
        ci = cell_c+c
        ri = cell_r+r
        if 0 <= c < C and 0 <= r <= R:
            draw_cell_by_cr(canvas, ci, ri, color)


win = tk.Tk()

win.geometry('330x600+400+20')
win.iconbitmap('图标.ico')

String_Var_FPS = tk.StringVar()
String_Var_FPS.set(f'FPS:{FPS}')
ttk.Label(win, textvariable=String_Var_FPS).pack()

score = 0
win.title(f'得分：{score}')
String_Var_score = tk.StringVar()
# String_Var_score.set(f'得分：{score}')
tk.Label(win, textvariable=String_Var_score).pack()

canvas = tk.Canvas(win, width=width, height=height)
canvas.pack()

draw_board(canvas, block_list)
# draw_cells(canvas, 3, 3, SHAPES['O'], SHAPESCOLOR['O'])
# draw_cells(canvas, 3, 8, SHAPES['S'], SHAPESCOLOR['S'])
# draw_cells(canvas, 3, 13, SHAPES['T'], SHAPESCOLOR['T'])
# draw_cells(canvas, 8, 3, SHAPES['I'], SHAPESCOLOR['I'])
# draw_cells(canvas, 8, 8, SHAPES['L'], SHAPESCOLOR['L'])
# draw_cells(canvas, 8, 13, SHAPES['J'], SHAPESCOLOR['J'])
# draw_cells(canvas, 5, 18, SHAPES['Z'], SHAPESCOLOR['Z'])


def draw_block_move(canvas, block, directiom=[0, 0]):
    shape_type = block['kind']
    c, r = block['cr']
    cell_list = block['cell_list']

    draw_cells(canvas, c, r, cell_list)

    dc, dr = directiom
    new_c, new_r = c+dc, r+dr
    block['cr'] = [new_c, new_r]

    draw_cells(canvas, new_c, new_r, cell_list, SHAPESCOLOR[shape_type])

# a_block = {
#     'kind': 'O',  # 类型
#     'cell_list': SHAPES['O'],  # 各个方格的坐标
#     'cr': [3, 3]  # 位置、方向
# }
#
#
# draw_block_move(canvas, a_block)


def generate_new_block():
    kind = random.choice(list(SHAPES.keys()))
    cr = [C//2, 0]
    new_block = {
        'kind': kind,
        'cell_list': SHAPES[kind],
        'cr': cr
    }

    return new_block


def check_move(block, direction=[0, 0]):
    cc, cr = block['cr']
    cell_list = block['cell_list']

    for cell in cell_list:
        cell_c, cell_r = cell
        c = cell_c + cc + direction[0]
        r = cell_r + cr + direction[1]

        if c < 0 or c >= C or r >= R:
            return False

        if r >= 0 and block_list[r][c]:
            return False
    return True

def horizontal_move_black(event):
    direction = [0, 0]
    if event.keysym == 'Left':
        direction = [-1, 0]
    elif event.keysym == 'Right':
        direction = [1, 0]
    # elif event.keysym == 'Down':
    #     # 最好不要用
    #     direction = [0, 1]
    else:
        return
    global current_block
    if current_block is not None and check_move(current_block, direction):
        draw_block_move(canvas, current_block, direction)



def rotate_block(event):
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    rotate_list = []
    for cell in cell_list:
        cell_c, cell_r = cell
        rotate_cell = [cell_r, -cell_c]
        rotate_list.append(rotate_cell)
    block_after_rotate = {'kind': current_block['kind'],
                          'cell_list': rotate_list,
                          'cr': current_block['cr']
                          }
    if check_move(block_after_rotate):
        cc, cr = current_block['cr']
        draw_cells(canvas, cc, cr, current_block['cell_list'])
        draw_cells(canvas, cc, cr, rotate_list, SHAPESCOLOR[current_block['kind']])
        current_block = block_after_rotate


def land(event):
    global current_block
    if current_block is None:
        return

    cell_list = current_block['cell_list']
    cc, cr = current_block['cr']
    min_height = R
    for cell in cell_list:
        cell_c, cell_r = cell
        c, r = cell_c+cc, cell_r+cr
        if block_list[r][c]:
            return

        h = 0
        for ri in range(r+1, R):
            if block_list[ri][c]:
                break
            else:
                h += 1
        if h < min_height:
            min_height = h

    down = [0, min_height]
    if check_move(current_block, down):
        draw_block_move(canvas, current_block, down)


score = 0
win.title(f'得分：{score}')
String_Var_score = tk.StringVar()
tk.Label(win, textvariable=String_Var_score).pack()

def aaaa(event):
    global FPS
    global zt
    if event.keysym == 'q':
        FPS -= 100
    elif event.keysym == 's':
        FPS += 100
    String_Var_FPS.set(f'FPS:{FPS}')


def check_row_complete(row):
    for cell in row:
        if cell == '':
            return False

    return True


def check_and_clear():
    global FPS
    has_complete_row = False
    for ri in range(len(block_list)):
        if check_row_complete(block_list[ri]):
            has_complete_row = True
            if ri > 0:
                for cur_ri in range(ri, 0, -1):
                    block_list[cur_ri] = block_list[cur_ri-1][:]
                block_list[0] = ['' for j in range(C)]
            else:
                block_list[ri] = ['' for j in range(C)]

            global score
            global String_Var_score
            score += 10
    if has_complete_row:
        draw_board(canvas, block_list)
        if FPS != 100:
            FPS -= 10
        win.title(f'得分：{score}')


# String_Var_score.set(f'得分：{score}')




def game_loop():
    win.update()
    global current_block
    global FPS
    if current_block is None:
        new_block = generate_new_block()
        draw_block_move(canvas, new_block)
        current_block = new_block
        if not check_move(current_block):
            messagebox.showinfo('Game over!', f'你的分数是：{score}')
            win.destroy()
            return
    else:
        if check_move(current_block, [0, 1]):
            draw_block_move(canvas, current_block, [0, 1])
        else:
            save_to_block_list(current_block)
            current_block = None


    check_and_clear()
    win.after(FPS, game_loop)

current_block = None

canvas.focus_set()
canvas.bind("<KeyPress-Left>", horizontal_move_black)
canvas.bind("<KeyPress-Right>", horizontal_move_black)
canvas.bind("<KeyPress-Down>", land)
canvas.bind("<KeyPress-Up>", rotate_block)
canvas.bind("<KeyPress-q>", aaaa)
canvas.bind("<KeyPress-s>", aaaa)
# canvas.bind("<KeyPress-space>", aaaa)

game_loop()
win.mainloop()
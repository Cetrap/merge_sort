from tkinter import *
from tkinter import ttk
from random import randrange as rr
from settings import *
from algorithms import mergeSort


window = Tk()
window.title("Merge Sort (Zhetibay Dulat 9 М)")
window.geometry(f"{WIN_W}x{WIN_H}")
window.config(bg=BLACK)

speed_name = StringVar()
speed_list = ['fast', 'medium', 'slow']


data = []


def draw_data(data, color_array):
    canvas.delete("all")
    canvas_width = WIN_W
    canvas_height = 500
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

    window.update_idletasks()


def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = rr(1, 150)
        data.append(random_value)

    draw_data(data, [WHITE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'slow':
        return 0.3
    elif speed_menu.get() == 'medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    time_tick = set_speed()

    mergeSort.merge_sort(data, 0, len(data) - 1, draw_data, time_tick)


UI_frame = Frame(window, width=WIN_W, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=0, pady=0)

l1 = Label(UI_frame, text="sorting speed: ", bg=WHITE)
l1.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

b1 = Button(UI_frame, text="sort", command=sort, bg=LIGHT_GRAY, width=10, height=2)
b1.grid(row=2, column=1, padx=5, pady=5)

b2 = Button(UI_frame, text="generate", command=generate, bg=LIGHT_GRAY, width=13, height=2)
b2.grid(row=2, column=0, padx=5, pady=5)

canvas = Canvas(window, width=WIN_W, height=500, bg=BLACK)
canvas.grid(row=1, column=0, padx=0, pady=0)

window.resizable(False, False)
window.mainloop()

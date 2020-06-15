#!/usr/bin/python

from __future__ import division
from Tkinter import Button, Entry, Frame, Tk, END

input_val = 0
prev_input_val = 0
operator = None


def handle_btn_click(e):
    def process_event():
        if isinstance(e, int):
            handle_int(e)
        else:
            handle_str(e)
    return process_event


def handle_int(n):
    global input_val
    input_val = (input_val * 10) + n
    change_display(input_val)


def handle_str(s):
    global input_val, prev_input_val, operator
    if s in '/*-+':
        prev_input_val = input_val
        input_val = 0
        operator = s
        change_display(input_val)
    elif s == 'c':
        prev_input_val = 0
        input_val = 0
        operator = None
        change_display(input_val)
    else:
        input_val = eval(str(prev_input_val) + operator + str(input_val))
        prev_input_val = 0
        operator = None
        change_display(input_val)


def change_display(v):
    txt_display.delete(0, END)
    txt_display.insert(0, v)

root = Tk()
root.title('Tk Calculator')
root.resizable(width=False, height=False)

frm_display_container = Frame(root)
frm_display_container.grid(row=1, column=1)

frm_input_container = Frame(root)
frm_input_container.grid(row=2, column=1)

txt_display = Entry(frm_display_container)
txt_display.insert(0, 0)
txt_display.grid()

input_values = [
    [1, 2, 3, '/'],
    [4, 5, 6, '*'],
    [7, 8, 9, '-'],
    ['c', 0, '=', '+']
]

for row_index in range(len(input_values)):
    row = input_values[row_index]
    for col_index in range(len(row)):
        val = row[col_index]
        Button(frm_input_container,
               text=val,
               padx=10,
               pady=10,
               command=handle_btn_click(val)).grid(row=row_index,
                                                   column=col_index)

root.mainloop()

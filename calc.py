#!/usr/bin/python

from Tkinter import *

input_values = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', '*'],
    ['7', '8', '9', '-'],
    ['c', '0', '=', '+']
]
curr_value = ''
prev_value = ''
operator = None

root = Tk()

frm_display = Frame(root)
frm_display.grid(row=0)

frm_input = Frame(root)
frm_input.grid(row=1)

txt_input = Entry(frm_display)
txt_input.grid()


def handle_click(v):
    def process_input():
        if v.isdigit():
            handle_digit(v)
        else:
            handle_alpha(v)
    return process_input

def handle_digit(n):
    global curr_value
    curr_value += n
    change_display(curr_value)

def handle_alpha(s):
    global curr_value, prev_value, operator
    if s in '/*-+':
        operator = s
        prev_value = curr_value
        curr_value = ''
        change_display(curr_value)
    elif s == '=':
        curr_value = str(eval(prev_value + operator + curr_value))
        prev_value = ''
        operator = None
        change_display(curr_value)
    else:
        curr_value = prev_value = ''
        operator = None
        change_display(curr_value)

def change_display(v):
    txt_input.delete(0, END)
    txt_input.insert(0, v)

for row_index in range(len(input_values)):
    row = input_values[row_index]
    for col_index in range(len(row)):
        val = row[col_index]
        Button(frm_input,
               text=val,
               padx=12,
               pady=12,
               command=handle_click(val)).grid(row=row_index, column=col_index)

root.mainloop()

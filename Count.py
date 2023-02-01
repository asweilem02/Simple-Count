import tkinter as tk
from tkinter import ttk

count = 0

def addone():
    global count

    count = count + 1

    label.configure(text=f'Count: {count}')

def subone():
    global count
    count = count - 1
    label.configure(text=f'Count: {count}')


windows = tk.Tk()
windows.title("Simple Count")

label = tk.Label(windows)
label.grid(column=3, row=0)

plus_button = ttk.Button(windows, text="+", command=addone)
plus_button.grid(column=4, row=1)

sub_button = ttk.Button(windows, text="-", command=subone)
sub_button.grid(column=2, row=1)



windows.mainloop()
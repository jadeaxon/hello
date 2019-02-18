from tkinter import *
from tkinter import ttk

def button_handler():
    print("Button pushed.")

root = Tk()

button1 = ttk.Button(root, text="Button 1")
button1.grid(column=1, row=1)

button2 = ttk.Button(root, text="Button 2", command=button_handler)
button2.grid(column=1, row=2)

root.mainloop()

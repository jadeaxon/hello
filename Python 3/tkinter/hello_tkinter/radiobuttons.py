from tkinter import *
from tkinter import ttk

root = Tk()

title = ttk.Label(root, text="Choose a flavor:")
title.grid(column=1, row=1, sticky=(N))

flavor = StringVar()
flavor.set('vanilla')

flavor1 = ttk.Radiobutton(root, text="Chocolate", variable=flavor, value='chocolate')
flavor2 = ttk.Radiobutton(root, text="Vanilla", variable=flavor, value='vanilla')
flavor3 = ttk.Radiobutton(root, text="Strawberry", variable=flavor, value='strawberry')

flavor1.grid(column=1, row=2, sticky=(W))
flavor2.grid(column=1, row=3, sticky=(W))
flavor3.grid(column=1, row=4, sticky=(W))

# Label to display the selected value of the radio button group.
label = ttk.Label(textvariable=flavor)
label.grid(column=1, row=5)

root.mainloop()

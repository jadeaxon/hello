from tkinter import *
from tkinter import ttk

root = Tk()

title = ttk.Label(root, text="Favorite flavor: ")
title.grid(column=1, row=1, sticky=(N))

flavor = StringVar()
flavor.set('vanilla')

flavor_input = ttk.Entry(textvariable=flavor)

flavor_input.grid(column=2, row=1, sticky=(W))

# Label to display the selected value of the radio button group.
flavor_label = ttk.Label(textvariable=flavor)
flavor_label.grid(column=1, row=3, sticky=(E))

password = StringVar()
password_label = ttk.Label(text="Password: ")
password_label.grid(column=1, row=4, sticky=(E))
password_input = ttk.Entry(textvariable=password, show="*")
password_input.grid(column=2, row=4, sticky=(W, E))

root.mainloop()

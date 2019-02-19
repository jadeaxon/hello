from tkinter import *
from tkinter import ttk

root = Tk()

# Make the root window 200x200 at position (50, 50)
root.geometry('200x200+50+50')

# By default, columns and grids have a weight of 0.
# This means that their widgets won't expand (even if sticky is set).
# When a window expands, a column expands in proportion of its weight to the sum of all columns weights.
# So, if all columns have a weight of 1, all widgets will expand (if sticky is set).
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# frame = ttk.Frame(root)
# frame.grid(column=0, row=0, sticky=(N, S, E, W))

w1 = ttk.Label(root, text="N S E W", background="blue")
# You can add padding so a widget doesn't entirely fill up a cell.
w1.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)

w2 = ttk.Label(root, text="E W", background="green")
w2.grid(column=0, row=1, sticky=(E, W))

w3 = ttk.Label(root, text="N S", background="yellow")
w3.grid(column=1, row=0, sticky="ns")

# Default stickness is none.  Widget will center in its grid cell.
w4 = ttk.Label(root, text="default", background="purple")
w4.grid(column=1, row=1)

# A widget can span multiple rows and/or columns.
# A widget can have a border of some number of pixels.  The relief option determines how it will be displayed.
w5 = ttk.Label(root, text="multirow N S E", background="pink", border=5, relief="sunken")
w5.grid(column=2, row=0, rowspan=3, sticky="nse")

w6 = ttk.Label(root, text="(0, 2) multicolumn", background="red")
w6.grid(column=0, row=2, columnspan=2, sticky="ew")

root.mainloop()

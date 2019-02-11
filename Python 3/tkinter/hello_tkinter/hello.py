from tkinter import *
# Themed Tk widgets.
from tkinter import ttk

# Create root window.
root = Tk()
# Add a button to it.
# What's grid() all about?
ttk.Button(root, text="Hello, Tkinter!").grid()

# Start the GUI event loop.
root.mainloop()

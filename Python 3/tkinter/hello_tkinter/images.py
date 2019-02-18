from tkinter import *
from tkinter import ttk

root = Tk()

image = PhotoImage(file="ascii_art.gif")

# The label widget does not fully support animated gifs.
label = ttk.Label(root, text="Display an image.")
label.grid() # grid() doesn't return the label widget, so we can't chain it above.
label['image'] = image

root.mainloop()



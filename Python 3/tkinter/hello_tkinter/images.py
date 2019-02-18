from tkinter import *
from tkinter import ttk

root = Tk()

image = PhotoImage(file="ascii_art.gif")

# The label widget does not fully support animated gifs.
# Using the 'compound' option, the image can be displayed below the text.
label = ttk.Label(root, text="Display an image in a label.", compound='bottom')
label.grid() # grid() doesn't return the label widget, so we can't chain it above.
label['image'] = image

root.mainloop()



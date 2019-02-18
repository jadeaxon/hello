from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root, text="This is the first label.")
label1.grid(column=1, row=1)

# The label widget does not fully support animated gifs.
# Using the 'compound' option, the image can be displayed below the text.
image = PhotoImage(file="images/ascii_art.gif")
label2 = ttk.Label(root, text="Display an image in a label.", compound='bottom')
label2.grid(column=1, row=2) # grid() doesn't return the label widget, so we can't chain it above.
label2['image'] = image

root.mainloop()

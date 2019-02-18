from tkinter import *
from tkinter import ttk

# PRE: pip install pillow
# This was already installed by default (or by something else) for me.
from PIL import Image
from PIL import ImageTk

def button_handler():
    print("Button pushed.")

root = Tk()

button1 = ttk.Button(root, text="Button 1")
button1.grid(column=1, row=1, sticky=(NW))

button2 = ttk.Button(root, text="Button 2", command=button_handler)
button2.grid(column=1, row=2)

width = 50
height = 50
img = Image.open("images/checkmark.png")
img = img.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)

button3 = ttk.Button(root, text="Button 3", image=image, compound='right')
# You can use either normal functions or lambdas as callbacks.
# You can set configuration options in the constructor or by map key notation.
button3['command'] = lambda: print("Anonymous function.")
button3.grid(column=2, row=1)

root.mainloop()

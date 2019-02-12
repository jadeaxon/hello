from tkinter import *
from tkinter import ttk

# Convert feet to meters.
# Being a function triggered by a button command, there are probably various args passed in.
# We're ignoring all of them for now.
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass

# Create a root window and give it a title.
root = Tk()
root.title("Feet to Meters")

# The frame is the main panel which holds the other widgets.
# Since a window itself isn't themed it makes sense to use a themed frame to contain all the other widgets.
mainframe = ttk.Frame(root, padding="3 3 12 12")

# A widget does not show up immediately when created.
# You have to tell it where in its parent's layout you want it via grid().
# The column and row are zero-based.
# The stick arg says what side(s) of the grid cell to align with.
# In this case, we're saying "put the frame in cell (0, 0) and align with all edges."
# Since no other grid cells are defined in the window, this effectively takes up the whole window.
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# This makes it so that if the window is resized, the frame will stretch to fill it.
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# These are Tk vars that can be bound to widget fields via their textvariable attribute.
# Yeah, these are two-way data bind variable similar to AngularJS $scope vars.
feet = StringVar()
meters = StringVar()

# Add a text entry field to the main frame.
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)

# It looks like the grid() method says where a child should go within its parent's grid layout.
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Set the button command to the calculate() function defined above.
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Set some padding for each of the main frame's child widgets.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Put the keyboard focus on the text entry widget for feet.
feet_entry.focus()

# Make it so when you press enter, the calculate function is executed.
root.bind('<Return>', calculate)

# Start the GUI event loop.
root.mainloop()

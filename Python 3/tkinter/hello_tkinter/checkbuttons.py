from tkinter import *
from tkinter import ttk

root = Tk()

def opinionChanged():
    print("The checkbox was activated.")

opinion = StringVar()
opinion.set('vanilla')

checkbox = ttk.Checkbutton(
    root,
    text='Which flavor?',
    command=opinionChanged, # Callback for when checkbox is clicked.
    variable=opinion, # Bind UI on/off state to a variable.
    # Clicking the checkbox automatically toggles it between these two values.
    onvalue='vanilla', # Defaults to 1 if not set.
    offvalue='chocolate' # Defaults to 0 if not set.
)
checkbox.grid(column=1, row=1)

# Label to display the onvalue or offvalue of the checkbox.
label = ttk.Label(textvariable=opinion)
label.grid(column=1, row=2)

root.mainloop()

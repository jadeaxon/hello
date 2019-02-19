from tkinter import *
from tkinter import ttk

root = Tk()

def flavorSelectionChanged(e):
    print("Selection changed.")
    print(e) # Yes, a VirtualEvent object is passed in.
    print(flavor_combo.current()) # Show 0-based index of current selection.

flavor = StringVar()
flavor_label = ttk.Label(text="Choose your flavor: ")
flavor_label.grid(column=1, row=1, sticky=(E))
flavor_combo = ttk.Combobox(textvariable=flavor)

# Provide preset values via list or tuple.
flavor_combo['values'] = ['chocolate', 'vanilla', 'strawberry', 'mint']
flavor_combo['values'] = ('chocolate', 'vanilla', 'strawberry', 'mint')

# Bind virtual event to handler function.
# Virtual events are high-level (non-OS) events that widgets emit.
flavor_combo.bind('<<ComboboxSelected>>', flavorSelectionChanged)

flavor_combo.grid(column=2, row=1, sticky=(W))



root.mainloop()

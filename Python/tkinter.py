#!/usr/bin/env python

# Simplest GUI example possible.
# Tkinter is Python's interface to Tk.  Thus Tkinter.
# Pronounced Tea Kay Inter.
# Tk is an extension of Tcl (tool control language).
# The whole thing provides a cross-platform GUI framework.
# Tkinter is the defacto GUI framework for Python.

# The nice thing about this is that in Cygwin (even running from the Cygwin python)
# this brings up an actual Windows window instead of trying to do some X Windows.

from Tkinter import Label
widget = Label(None, text='Hello, Tkinter!')
widget.pack()
widget.mainloop()


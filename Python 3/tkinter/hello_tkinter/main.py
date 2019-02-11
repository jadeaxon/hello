import tkinter

# PRE: You've installed ActiveState ActiveTcl.

# Print the Tkinter version.
version = tkinter.Tcl().eval('info patchlevel')
print(version)

tkinter._test()




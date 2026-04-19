#!/usr/bin/env python3

# A variable is a named object reference.
# It does not hold the object itself, just a reference to it.
# It's like a pointer in other languages, but not statically typed. Can refer to anything.

# Have the name x in the current module/namespace refer to an integer with value 1.
# Assign object created from literal 1 to name x in the __main__ module (if running this file as a
# script).
# If importing this as a module, x is variable.x.
# A variable springs into existence as soon as you assign to it. No need to declare it in advance.
x = 1

# A script doesn't automatically have access to __main__ explicitly, but you can import it.
import __main__
__main__.x = 2

# You can see that x and __main__.x are really the same name.
print(x)

# See what names are bound/assigned in current namespace.
variables = dir()
print(variables)

# A variable can point to any kind of object.
x = 2.3 # float
x = [1, 2, 3] # list
x = "a string" # string

# You can delete a variable. Causes it to no longer exist.
del x

# You get a NameError if you try to access a variable that does not exist.
try:
    print(x)
except NameError as e:
    print("You tried to use variable x after it was deleted. It does not currently exist.")

x = 2 # x exists again
print(x)




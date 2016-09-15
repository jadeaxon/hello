#!/usr/bin/python3

# Unlike in Python 2, you need to use () with print.
print("Put", "space", "between", "args.")
print("Automatically append a newline.")
print("Suppress newline with the named arg 'end'", end="")
print(" as above.")

name = "Jeff"
age = 40
# printf style format string with % operator to bind a tuple to formatter.
print("%s is %d." % (name, age)) 
# A Pythonic format string.
print("{0} is {1}.".format(name, age))



#!/usr/bin/env python3

# Import a specific symbol from a module into current namespace.
from sys import argv

# Read the WYSS section for how to run this.
# Read from the "argument variable", an array.
script, first, second, third = argv
# Combine command-line args and user input.
fourth = input("Enter 4th arg: ")
# Script name.
print("The script is called: ", script)
# First arg.
print("Your first variable is: ", first)
# Second arg.
print("Your second variable is: ", second)
# Third arg.
print("Your third variable is: ", third)
# Fourth arg (user-entered).
print("Fourth arg (user-entered): ", fourth)


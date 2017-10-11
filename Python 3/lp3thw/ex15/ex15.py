#!/usr/bin/env python3

# Get file name as command-line arg.
from sys import argv
script, filename = argv

# Open the file.  We now have a file object, txt.
txt = open(filename)

# Dump the contents of the file.
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# Ask for another file name.
print("Type the filename again:")
file_again = input("> ")
# Open file and print its contents.
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()



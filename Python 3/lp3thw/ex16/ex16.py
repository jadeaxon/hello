#!/usr/bin/env python3

# Import argv for command-line args.
from sys import argv

# Unpack the command-line args.
script, filename = argv

# Warn about erasing file supplied on command line.
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Wait for <Enter> or ^C to be pressed.
input()

# Open the file.
print("Opening the ile...")
target = open(filename, 'w')

# Truncate the file.
print("Truncating the file.  Goodbye!")
target.truncate()

# Ask for things to write.
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Write stuff to the truncated file.
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file.
print("And finally, we close it.")
target.close()



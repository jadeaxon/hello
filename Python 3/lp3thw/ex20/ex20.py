#!/usr/bin/env python3

# Get the command-line args.
from sys import argv
script, input_file = argv

# Print the whole file.
def print_all(f):
    print(f.read())

# Rewind to the beginning of the file.
def rewind(f):
    f.seek(0)

# Print the next line and a line count.
# Having to pass in this line count is fail.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open file and print.
current_file = open(input_file)
print("First, let's print the whole file:\n")
print_all(current_file)

# Rewind and print a few lines.
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)


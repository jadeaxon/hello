#!/usr/bin/env python3

# Open a file for reading.  Echo each line to stdout.
# Default encoding is UTF-8.
f = open('/etc/hosts', 'r')
while True:
	line = f.readline()
	if line:
		print(line, end="")
	else:
		break
f.close()

# Better to use 'with' when working with files.
with open('/etc/hosts', 'r') as f:
    contents = f.read() # Read entire contents of file into a string.
print(len(contents))


# The file object acts as an iterator on the lines in the file.
lines = 0
with open('/etc/hosts', 'r') as file:
    for line in file:
        lines += 1
print(lines)


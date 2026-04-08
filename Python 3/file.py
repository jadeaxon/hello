#!/usr/bin/python3

# Open a file for reading.  Echo each line to stdout.
f = open('/etc/hosts', 'r')
while True:
	line = f.readline()
	if line:
		print(line, end="")
	else:
		break
f.close()


#!/usr/bin/env python3

# print()
# See hello/python3/print.py
print("Hello, builtin functions!")
print()

# input()
# See hello/python3/input.py

# round()
f = 13 / 3
print(f)
f = round(f, 2) # Round to 2 decimal places
print(f)
print()

# float()
# convert to float (float constructor)
i = 3
f = float(i)
print(f)
s = "3.27"
f = float(s)
print(f)

# int()
# convent to int (int constructor)
# Will call __index__ method of an object.
s = "32"
i = int(s)
print(i)
f = "3.1"
# NO: i = int(f)
print(i)

# int() takes a base arg that is 10 by default.
i = int("FF", 16) # convert base 16 (hex) to int
print(i)




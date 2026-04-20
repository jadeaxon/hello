#!/usr/bin/env python3

# Convert to int.
int(3.7) # 3
int("3") # Convert string to int.
# int("3.4") # Value Error
int("101", 2) # Convert base 2 string (binary) to int.
5
int("70", 8) # Convert base 8 string (octal) to int.
56
int("FE", 16) # Convert base 16 string (hex) to int.
254
int("0xFE", 16) # You can include the binary, octal, and hex literal prefix.
254
# int("foo") # Raises a ValueError.

# Convert to float.
float(3) # 3.0
float("3.4") # Convert string to float.

# Convert to str.
str(12) # Convert number to string.
str(3.4)
str(["a", "list"])

# Convert any iterable to list.
t = (1, 2, 3)
L = list(t)

# Convert any iterable to tuple.
L = [1, 2, 3]
t = tuple(L)

# Convert any object to boolean.
# calls o.__bool__()
# if no bool, checks o.__len__ != 0 (empty things are false)
bool(1)
bool([])
bool(["not empty"])



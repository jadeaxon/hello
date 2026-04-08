#!/usr/bin/env python3

s = "This is a string."
s = 'This is also a string.'
s = s + " With stuff appended." # + operator joins strings.
print(s)
t = type(s)
print(t)

s = "echo "
s = s * 3 # * operator repeats strings.
print(s)

x = 3
s = f"The value of x is {x}." # Use f-strings to interpolate variables inside strings.
print(s)

# Multiline string.
mls = \
"""
Multiline
string
"""
print(mls, end="")

# Multiline f-string.
fmls = \
f"""
The value of x is:
{x}
"""
print(fmls, end="")






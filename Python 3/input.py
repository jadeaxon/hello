#!/usr/bin/env python3

# In Python 3, input() is safe.  In Python 2, you had to use raw_input().
name = input("What is your name? ")
age = int(input("How old are you? "))

template = str('Hi, {0}, how does it feel to be {1}?')
message = template.format(name, age)

print(message)

# You can use input with no args. And use print() to prompt user.
print("Enter a string:")
# Input always returns a string. It removes the trailing newline.
s = input()
print(s[-1])

# If you want an int or float, you need to convert the string you get back from input().
print("Enter a float:")
s = input()
f = float(s)
print(f)


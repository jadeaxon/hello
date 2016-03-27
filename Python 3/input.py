#!/usr/bin/env python3

# In Python 3, input() is safe.  In Python 2, you had to use raw_input().
name = input("What is your name? ")
age = int(input("How old are you? "))

template = str('Hi, {0}, how does it feel to be {1}?')
message = template.format(name, age)

print(message)

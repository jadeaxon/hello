#!/usr/bin/env python3

centimeters_per_inch = 2.54
kilograms_per_pound = 0.454

# All the vars used to be prefixed with my_.
# At some point, that will most likely be used to introduce OOP.
name = 'Jeff Anderson'
age = 41 # The sad truth.
height = 72 # inches
centimeters = height * centimeters_per_inch
weight = 195.4 # lbs
kilograms = weight * kilograms_per_pound
eyes = 'hazel'
teeth = 'white enough'
hair = 'gone'


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {centimeters} centimeters tall.")
print(f"He weighs {weight} pounds.")
print(f"He weighs {kilograms} kilograms.")
print(f"That's technically overweight for his height.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the toothpaste.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, then I get {total}.")


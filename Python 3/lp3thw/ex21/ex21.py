#!/usr/bin/env python3

# Define some arithmetic functions.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# Do some math with functions.
print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# Function calls as function args.
# age + (height - (weight * (iq / 2)))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = add(iq, multiply(weight, divide(height, subtract(age, 2))))

# ((iq + weight) / (age - height)) * 2
what3 = multiply(
    divide(
        add(iq, weight),
        subtract(age, height)
    ),
    2
)

print("That becomes:", what, "Can you do it by hand?")
print(f"what2 = {what2}")
print(f"what3 = {what3}")



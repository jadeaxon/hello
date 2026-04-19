#!/usr/bin/env python3

import itertools

# A generator function returns a generator.
# A generator is iterable, but can only be iterated over once.
# Use the generator function to get a new generator if needed.
# A bit confusingly, the generator runs the code in the generator function definition.
# It's kind of like the function is implicitly decorated due to using yield.
# Saves state between calls and yields one result at a time.

# A generator function that yields 0, 3, 6, 9, etc.
def g_infinite():
    x = 0
    # If you don't use a loop, the generator will implicitly return causing a StopIteration.
    while True:
        x += 3
        yield x # Return value but save function state

def g_finite():
    x = 0
    while True:
        x += 3
        if x > 60:
            return # Implicitly raise StopIteration
        yield x

# The generator function returns a generator that you can then iterate over.
generator = g_infinite()

for v in generator:
    if v > 30: break
    print(v)

generator = g_finite()
for v in generator:
    print(v)

# You can also do generator comprehensions to get a generator.
print("Using generator comprehension (finite sequence):")
generator = (x * 3 for x in range(20))
for v in generator:
    print(v)

print("Using generator comprehension (infinite sequence):")
# Infinite generator of even numbers
generator = (x * 3 for x in itertools.count(start=0, step=1))
for v in generator:
    if v >= 300: break
    print(v)

# Get the first true object in a list.
# Actually using a generator comprehension.
# Inside a function call, its enclosing ()s can be omitted.
# next() gets the first value from the generator.
L = [0, [], "true", True]
o = next(e for e in L if e)
print(o)



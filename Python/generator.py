#!/usr/bin/env python

# Python has special functions called generators.
# All a generator is is an object with a next() method that resumes where it left off each time it is called.
# Defining a function using yield creates a factory method that lets you create a generator.
# Instead of using 'return' to return a value, you use 'yield'.
# That's it!


def g(step, max_steps):
    i = 0
    steps = 0 # Steps completed.
    while True:
        if steps >= max_steps: break
        yield i
        i += step
        steps += 1

generator = g(3, 10)
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print

# Generators work well in for loops.
for value in g(5, 30):
    print value


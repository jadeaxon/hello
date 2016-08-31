#!/usr/bin/env python

# Using the lambda keyword, you can define small anonymous function objects.
# Thus, you can make a function that returns a function.

# Returns a function that increments whatever you pass it by n.
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(10)

print f(0)
print f(1)


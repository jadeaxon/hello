#!/usr/bin/env python

# You can have tuples also.  They are not exactly the same as lists.
triplet = 1, 2, 3
print triplet

# Use a trailing comma to make a singleton.
singleton = 1,
print singleton

# Tuples are immutable like strings.

# A tuple can be nested.
nested = 1, (1, 2, 3), 3
print nested


# You can unpack a tuple into normal variables.
first, second, third = triplet
print first, second, third


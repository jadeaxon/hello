#!/usr/bin/env python3

import random

l = [] # empty list
l = [1, 2, 3]

# Loop over the elements of the list.
for e in l: print(e)
print()

# Remove the last element of the list.
print(l)
print(len(l)) # Get length of list.
del l[-1]
print(l)
print(len(l))
print()

# Append to list.
l.append(3)
l.append(4)
print(l)

# Insert into list.
l.insert(0, 0) # list.insert(location, value)
print(l)

rli = reversed(l) # Create a reverse iterator for the list (not the same as a reversed actual list).
l.reverse() # Reverse the list in place.

l2 = l[:] # Copy a list (via list slice).
print(l)
print(l2)

if l is not l2:
    print("We have copied the list.")

# Shuffle a list.
random.shuffle(l)
print(l)

# Convert a string to list of characters (length 1 strings).
characters = list("a string")
print(characters)





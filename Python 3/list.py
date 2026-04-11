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

# Swap the first and last elements of the list.
l[0], l[-1] = l[-1], l[0]
print(l)

# Lists can contain various data types.
l = ["one", 2, 3.0]
print(l)

# List can be nested.
l = [1, [2, 3], 4]
print(l)
print()

# Check if something is in a list or not.
L = ["frog", "turtle"]
print("turtle" in L)
print("bee" not in L)
print()


#==============================================================================
# List Methods
#==============================================================================

print("Trying all the list methods.")
L = []
L2 = ["bar", "baz"]

# Append to end of list. You can only append one element at a time.
L.append("foo")
print(L)
# L.append("foo", "bar") # NO

# Append all elements of an iterable to end of list.
L.extend(L2)
print(L)
# L.extend("bar", "baz") # NO

# Shallow copy the list.
L3 = L.copy()
print(L3)

# Clear/empty the list.
L.clear()
print(L)

L = L3[:] # Copy via slice.

# Count number of times an equivalent object appears in list.
foos = L.count("foo")
print(foos)

# Get the index of a list element. ValueError if not present.
index = L.index("baz")
print(index)

# Insert something into list at specific location.
# Existing elements move right.
L.insert(0, "pre-foo") # Insert at beginning of list.
print(L)

# Remove and return (pop) element from specific location. Default is end of list (-1).
# Allows list to be used like a stack.
e = L.pop()
print(L); print(e)
e = L.pop(1)
print(L); print(e)
L = L3[:]

# Remove (without returning) first occurrence of given value. ValueError if not found.
L.remove("baz")
print(L)
L= L3[:]

# Reverse list in place.
L.reverse()
print(L)

# Sort in place.
# Named args: key, reverse. Assign key a function/lambda to control how sorted. Use reverse=True to reverse
# sort.
L.sort()
print(L)

# We'll sort by "weight" of each element. The sum of the values of its characters.
# Basically, whatever the key function returns given each element as an arg is sorted rather than
# the element values directly.
L = ["none", "one", "on", "o", "aaa"]
L.sort(key=lambda e: sum(map(ord, e)))
print(L)

# That's it. That is ALL the list methods.






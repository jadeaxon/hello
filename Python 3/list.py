#!/usr/bin/env python3

import random

L = [] # empty list
L = [1, 2, 3]

# Access list elements by integer index.
e = L[0] # first
e = L[1] # second

# Negative indexes work.
e = L[-1] # last (first to last)
e = L[-2] # second to last

# Trying to access an out of range index raises an IndexError.
try:
    e = L[77]
except Exception as e:
    print(e, type(e))

# The index can be any expression.
x = 0
y = 1
e = L[x + y]

# Loop over the elements of the list.
for e in L: print(e)
print()

# Remove the last element of the list.
print(L)
print(len(L)) # Get length of list.
del L[-1]
print(L)
print(len(L))
print()

# Append to list.
L.append(3)
L.append(4)
print(L)

# Insert into list.
L.insert(0, 0) # list.insert(location, value)
print(L)

rli = reversed(L) # Create a reverse iterator for the list (not the same as a reversed actual list).
L.reverse() # Reverse the list in place.

L2 = L[:] # Copy a list (via list slice).
print(L)
print(L2)

if L is not L2:
    print("We have copied the list.")

# Shuffle a list.
random.shuffle(L)
print(L)

# Convert a string to list of characters (length 1 strings).
characters = list("a string")
print(characters)

# Swap the first and last elements of the list.
L[0], L[-1] = L[-1], L[0]
print(L)

# Lists can contain various data types.
l = ["one", 2, 3.0]
print(L)

# List can be nested.
l = [1, [2, 3], 4]
print(L)
print()

# Check if something is in a list or not.
L = ["frog", "turtle"]
print("turtle" in L)
print("bee" not in L)
print()

# List slices.
# L[start:stop:step]
# stop is exclusive
# step can be negative
# leaving blank => None => include first/last depending on if step is + or -
# The args work pretty much the same as range() args.
print("List slice examples:")
L = ["first", "second", "third", "fourth", "fifth"]
L2 = L[:] # Copy of entire list.
L2 = L[0:] # Same.
L2 = L[0:2] # First two elements: L[0], L[1].
L2 = L[1:3] # L[1], L[2]
L2 = L[:-1] # All but the last element.
L2 = L[0:-1] # Same
L2 = L[::2] # Every other element, starting with first.
print(L2)
L2 = L[::-1] # Entire list, reversed.
print(L2)
L2 = L[::-2] # Every other element, starting with last.
print(L2)

# You can use the slice() function to get a slice object.
slice_object = slice(3, None) # [3:]
L2 = L[slice_object] # L[3:]
print(L2)

# You can delete slices. This affects original list.
del L[:] # Clear the entire list. List is now empty.

# You can assign to a slice. Replaces what was there.
L = ["first", "second", "third", "fourth", "fifth"]
L[1:3] = ["one", "two", "three"] # The replacement can be any size.
L[1:2] = [] # Same as del L[1]
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

# Is overriding __index__ enough to use any object as a list index?
# Yup, it is.
class First():
    def __index__(self):
        return 0

o = First()
L = ["first", "second", "third"]
first = L[o]
print(first)





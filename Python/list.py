#!/usr/bin/env python

# A variable can be set to refer to a list.
# All variables in Python are really references.
# Use [] notation to define a list literal.
# Python lists can contain mixed types.
L = ["element 0", "element 1", 2, 3]

print L

# Lists can use all the same subscripting and slicing that strings can.
print "L[0] => " + str(L[0])
print "L[-1] => " + str(L[-1])


# A slice returns a new list.
L2 = L[0:2]
print "L[0:2] =>", L2

# You can assign to subscripts including slices (string subscripts could not be assigned to).
# You can use the to shrink or erase sublists or just replace values.
L[0:2] = [0, 1]
print L

# len(list) gives you the length of a list.
print "len(L) => %s" % len(L)


# Lists have methods.
# Append an element to the end of a list.
L.append("appended")
print L

# Add all the elements from one list to the end of another.
otherList = ["some", "more", "stuff"]
L.extend(otherList)
print L

# Insert an element before the given index.
L.insert(0, "inserted")
print L

# Delete the first matching equivalent element.  The argument is not an index into the list.
L.remove(0)
print L

# Remove and return the element at the given index.
element = L.pop(0)
print L

# You can also use the 'del' operator to remove elements or slices.
L.append("thing to delete")
del L[-1]
print L

# Return index of first equivalent element to arg.
index = L.index("stuff")
print "'stuff' is at index %d." % index

# Count how many times the element appears in the list.  Lists may contain duplicates.
L.append("more")
instances = L.count("more")
print "There are %d instances of 'more' in list L." % instances

# Sort a list (mutates it).
# Not sure how Python does comparators.
L3 = [53, 22, 666, 1]
L3.sort()
print L3


# Reverse the elements in a list.
L3.reverse()
print L3

# You can filter a list using the built in filter function.
# filter(predicate, list) => filtered list
#
# This predicate returns true only if its arg is not divisible by 2 and 3.
def f(x): 
    return ((x % 2) != 0) and ((x % 3) != 0)

# The list filtered will contain all numbers between 2 and 24 inclusive that are neither divisible by 2 nor 3.
filtered = filter(f, range(2, 25))
print filtered

# You can map a function onto a list to produce a new list.
def cube(x): return x * x * x

cubes = map(cube, range(1, 11))
print cubes

# Mapping works for functions that accept more than one arg.  Just pass a list for each necessary arg.
args1 = range(8)
args2 = range(1, 9)
def add(x, y): return x + y

results = map(add, args1, args2)
print results

# You can reduce (summarize) a list to a single value by applying a binary function to the first two elements, and
# then applying the binary function to that result and the next element until no elements remain.
# For example, this computes the sum of a list of numbers.
def add(x, y): return x + y
total = reduce(add, range(1, 11)) # ((1 + 2) + 3) + 4 ...
print total


# Lists can be defined via 'list comprehensions'.  These can be clearer than using map and filter to achieve the same results.
# You use an expression followed by a for followed optionally by an if.  All inside [].
L = [3 * x for x in range(11) if x > 3]
print L

# A list comprehension can use multiple for loops.  
L = [x * y for x in range(1, 13) for y in range(1, 13)]
print L


# To get the index and element value in a loop, use 'enumerate'.
for index, value in enumerate(L):
    print index, value




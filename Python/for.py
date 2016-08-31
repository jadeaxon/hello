#!/usr/bin/env python

# Behind the scenes, the for statement calls iter() on the container object. 
# The function returns an iterator object that defines the method next() which accesses elements in the container one at a time.
# When there are no more elements, next() raises a StopIteration exception.
#
# If you define a class with the same iterable interface, it can also be used in for <element> in <container> statements.
# It's an example of syntactic sugar.


# Iterate over a list.
aList = ['cat', 'window', 'defenestrate']
for element in aList:
    print element, len(element)

print

# range(n) makes a list from 0 .. n-1 inclusive.
aList = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(aList)):
    print i, aList[i]

print

# Demonstration of continue and break.
for i in range(1, 100):
    if (i % 2) == 0:
        continue
    if i == 33:
        break
    print i

print

# Nested loops.
for x in range(3):
    for y in range(3):
        print "(%d, %d)" % (x, y)

#!/usr/bin/env python


# You can turn a list or a string into a set.
L = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
S = set(L) # Make a set from a list.
print S

# You can use the 'in' operator to test for set membership.
if 'apple' in S:
    print "There is an apple in set S."

if not 'pineapple' in S:
    print "There is no pineapple in S."


# You can do set operations on sets.
A = set('abracadabra')
B = set('alacazam')
print A
print B
print A - B # set difference
print A | B # union
print A & B # intersection
print A ^ B # non-intersection



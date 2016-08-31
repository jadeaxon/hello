#!/usr/bin/env python

# A dictionary is like a hash in Perl.  An assosciative array.

# You can use any immutable object as the hash key, not just strings.

D = {'jack': 4098, 'sape': 4139}
D['guido'] = 4127
print D
print D['jack']

del D['sape']
D['irv'] = 4127
print D
print D.keys()

# Check if a key is in the dictionary using the 'in' operator.
if 'guido' in D:
    print "Guido is in the dictionary."


# You can build a dictionary from a list of duples.  Using a list comprehension.
D = dict( [(x, x ** 2) for x in [2, 4, 6, 8]] )    
print D

# If you need to iterate over the keys and values, use 'iteritems'.  In Java, the pairs are called entries.
for key, value in D.iteritems():
    print key, value


# Access a dictionary without raising a KeyError when key DNE.
# 2nd arg to get() is the default value to return if key lookup fails.
value = D.get('key that DNE', None)



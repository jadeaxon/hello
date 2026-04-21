#!/usr/bin/env python3

s = set() # Empty set.
# s = {} # NO: This is an empty dictionary.
bool(s) # Empty set is false.

L = ["foo", "bar", "baz"]
s = set(L) # Pass any iterable to set().
print(s)

s = {'a', 'e', 'i', 'o', 'u'}
len(s)

# Set has no duplicates, so you can use it to unique other iterables.
repeats = "aaaeeiiooouu"
s = set(repeats)
print(s)

# Sets are not ordered. Nor do they have indexes.
# s[0] # NO

s2 = {'a', 'y', 'z'}

s3 = s | s2 # union
s3 = s.union(s2) # same
print(s3)
s3 = s & s2 # intersection
s3 = s.intersection(s2)
s.intersection_update(s2) # Modify to keep only common elements.
print(s3)

s = {'a', 'b', 'c'}
s.add('d')
print(s)

# However, + is not overloading for sets.
# NO: s + 'e'
# NO: s + s2

# update() mutates the original list whereas union() does not.
# update() is like |=; union() is like |.
s.update(s2)
for e in s:
    print(e)

# The shortcut assignment operators for sets do mutate the original set.
s = {'a', 'b', 'c'}
s2 = s
s |= {'e'}
print(s, s2) # Both have changed since |= did not create a new set.

s.remove('a') # KeyError if DNE
s.discard('a') # No error if DNE
print(s)

s2 = s.copy()
s.clear()
s = s2.copy()
print(s)

s2 = s.difference({'y', 'z'})
s2 = s - {'y', 'z'} # Same via operator.
print(s2)

s.difference_update({'y', 'z'}) # Remove elements.
print(s)

# Symmetric difference. Things that are only in one of the sets but not both.
s = {'a', 'b', 'c'}
s2 = {'b', 'c', 'd'}
s3 = s ^ s2
s3 = s.symmetric_difference(s2) # Same
s.symmetric_difference_update(s2)
print(s)
print(s3) # {'a', 'd'}

# Disjoint sets have no common elements.
s = {'a', 'b'}
s2 = {'c', 'd'}
b = s.isdisjoint(s2)
print(b) # True

# Subsets and supersets.
s = {'a'}
s2 = {'a', 'b', 'c'}
b = s.issubset(s2) # True
print(b)
b = s2.issuperset(s) # True
print(b)

s = {'foo', 'bar', 'baz'}
while s:
    e = s.pop()
    print(e)

# Create frozen set. Can be used in tuples since immutable.
s = {"ice cube", "popsicle", "glacier"}
fs = frozenset(s)
print(fs)

t = ("frosty", fs)
print(t)

# You can put normal sets in a tuple. Just better if you don't.
t = ("melty", s2)
print(t)





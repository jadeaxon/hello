#!/usr/bin/env python3

# Tuples are immutable sequences.
# But, they may contain immutable refs to mutable objects like lists.

t = ()
t = (1,) # Must use trailing comma for 1-tuples.
t = (1, 2)
t = ("one", 2)
t = 1, 2, 3 # Parenthesis are optional but more clear.

t = t + t # concat
t = t * 2 # repeat
print(t)

v = t[0]

# You can use tuple slices (but can't assign to them since tuple's are immutable).
t2 = t[:]

t = (1, 2, 3)
x, y, z = t # Assignment unpacking
print(x, y, z)

2 in t
4 not in t

L = sorted(t, reverse=True)
print(L)

t = tuple(L) # tuple(<iterable>)
print(t)

# Tuple comprehension.
t2 = (v + 1 for v in t) # Returns a generator, not a list.
print(t2)
print(tuple(t2))

# Tuple class has just two methods.
i = t.index(3) # Location of value 3 in tuple.
c = t.count(3) # Number of 3 values in tuple.




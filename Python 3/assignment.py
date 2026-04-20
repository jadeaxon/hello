#!/usr/bin/env python3

# Assign 1 to x.
x = 1

# Assign 0 to x, y, and z.
# Multiple binding. Not = right binding. = does not return a value.
# = is part of a statement, not an expression (like other operators).
# This is really syntactic sugar.
x = y = z = 0

# Tuple assignment/unpacking.
x, y, z = 1, 2, 3
(x, y, z) = (1, 2, 3)
print(x)
print(y)
print(z)

# Somewhat confusingly, this assigns the same tuple to all the variables.
x = y = z = "foo", "bar", "baz"
print(x)
print(y)
print(z)

# Iterables unpack.
L = [1, 2, 3]
x, y, z = L
print(x)

# You can NOT explicitly unpack the iterable here.
# x, y, z = *L # SyntaxError

# Either too many or too few values in the iterable is a problem.
# x, y = L # ValueError
# a, b, c, d = L # ValueError

# Nested tuple assignment/unpacking.
((a, b), (c, d)) = ((1, 2), (3, 4))
print(d)

# Works in for loops too.
L = [((3, 4), (5, 6))]
for ((a, b), (c, d)) in L:
    print(d)

# A simpler version of it in action.
# Tuple parenthesis omitted.
D = {"key": "value"}
for k, v in D.items():
    print(f"{k} = {v}")

# Function definitions do an implicit assignment to their name.
f = 3.75
def f(): pass
print(f)

# As do classes.
Foo = "foo"
class Foo(): pass
print(Foo)



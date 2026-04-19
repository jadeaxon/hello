#!/usr/bin/env python3

True # true literal/keyword
False # false literal/keyword

print(True == 1) # yes, it is
print(True is 1) # no it is not; so True is a different 1 used to represent boolean truth
print(False == 0) # yes
print(False is 0) # no

# True is an instance of class bool that is equal to int 1.
# bool is actually a subclass of int
t = type(True)
print(t)
q = isinstance(True, int)
print(q)

# Any object has a boolean interpretation.
# You can use bool(o) to get its boolean value. This calls o.__bool__() under the hood.
# Empty things are false. Lists, strings, etc.
# 0 and 0.0 are False; all other numbers are true.
objects = [0, 0.0, -0.0, [], {}, "", set(), None]
print("Things that are interpreted as false:")
for o in objects:
    b = bool(o)
    print(f"{o}: {b}")
print()

# Pretty much everything else is interpreted as true.
def func(): pass
objects = [1, -1, 3.7, ["element"], {"k": "v"}, "string", {"a"}, func]
print("Things that are interpreted as true:")
for o in objects:
    b = bool(o)
    print(f"{o}: {b}")
print()

class Deceiver():
    def __bool__(self):
        return False

print("Overriding __bool__ to implement truthiness of an object.")
deceiver = Deceiver()
b = bool(deceiver)
print(b) # False due to __bool__

# Binary logical operators do not necessarily evaluate explicitly to True or False.
r = 3 and 0 # Result will be the first false value or the last value.
print(r)
r = 0 or 1 # Result will be the first true value or the last value.
print(r)

# Is anything in the iterable true?
# Returns a boolean, not the first true value.
b = any([0, [], "one"])
print(b)

# Get the first true object in a list.
# Actually using a generator comprehension.
# Inside a function call, its enclosing ()s can be omitted.
# next() gets the first value from the generator.
L = [0, [], "true", True]
o = next(e for e in L if e)
print(o)

# Are all the things in the iterable true?
b = all([1, "two", 3.0])
print(b)








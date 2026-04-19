#!/usr/bin/env python3

# Unary plus. Rarely used.
+1

# Unary minus.
-1

# Binary plus. Addition.
# Operators actually call various dunder methods like __add__ under the hood.
# This lets you override operators in your own classes.
r = 1 + 1
r = int(1).__add__(1) # Same thing.
# NO: 1.__add__(1) # Can't call a method directly on an int literal.
print(r)

# For strings, it is concatenation.
s = "first string" + "second string"
print(s)

# Binary minus. Subtraction.
r = 1 - 1
print(r)

# You can't subtract strings.
try:
    s = "first string" - "second string"
except Exception as e:
    print(e)

# Numeric multiplication.
r = 3 * 2
print(r)

r = 3.3 * 2.0
print(r)

r = 3.2 * 2 # Mixing int and float results in float.
print(r, type(r))

# String replication.
r = "repeat me" * 3
print(r)



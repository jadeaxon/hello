#!/usr/bin/env python3

x = 3
y = 4

def f(x):
    # The x parameter shadows the global x.
    x = x + 1
    return x

def g():
    global z
    # Using global x and y. You can read them without using 'global' but can't assign to them.
    # Even though z isn't initialized outside this function, this should still work. Yup, it does.
    z = x * y
    return z

def h():
    # Try to assign to a global var without using 'global' and no parameter shadowing it.
    try:
        x = 0
    except Exception as e:
        print(e)
    return x # We can still read global x.
    # What actually happens here is that x becomes a local, non-parameter variable.
    # Even though in try block, it still has function scope, so it shadows global x in the return.

# Does using 'global' override parameter with same name?
# Can't do this: SyntaxError.
def i(x):
    ## global x # Illegal.
    x = x + 1
    return x

r = f(x)
print(r, "expected", 4)
print(x, "expected", 3)

r = g()
print(r, "expected", 12)

r = h()
# print(r, "expected", 3)
print(r, "expected", 0)





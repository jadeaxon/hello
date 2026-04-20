#!/usr/bin/env python3

# The true global scope in Python is the builtin scope.
# builtins can be seen from any file.
print("You can use the builtin function print anywhere.")

# Variables defined (assigning to them defines them) at the top level of a file
# are called global.
# They are only global to their file. You can't see them in other files.
# You have to import them as a module to access them.
x = 1 # new global variable

# Define a global variable system in this file that refers to the sys module
import sys as system
print(system.platform)

# You are in the __main__ module when you run a file as a script.
# But, you can't access it as __main__ unless you import it.
# No reason to actually do this other than for demonstration.
import __main__
__main__.x = 3
print(x) # x and __main__.x are actually the same variable

# Defining a function or class at the top level implicitly assigns it to a global variable.
f = "not a function"
def f(): pass
print(f)

MyClass = "not a class"
class MyClass(): pass
print(MyClass)

# You can delete global vars.
e = "set by except clause?" # actually *deleted* by except clause
del f
try:
    f()
except Exception as e:
    # except clauses each have their own local scope
    # NO: assigning the exception to e with as will not affect global var e
    # something weirder is happening
    # the exception clause does use the global variable e
    # but, it undefines e when it exits the clause
    # so, it's a weird hybrid of local and global scope
    print(e, type(e))
# print(e) # e not defined!

# Since defining a function is an implicit assignment, you can't have overloaded functions
# like in other languages. There is just one version of a function: the last one defined.
def f(): return 0
def f(x, y): return x + y
try:
    f() # not overloaded
except Exception as e:
    print(e, type(e))
r = f(1, 2) # Only the latest function definition for a given function name exists.
print(r)





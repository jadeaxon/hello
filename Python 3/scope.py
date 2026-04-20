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

# Each function invocation has its own local scope.
del x
def f():
    # x is only defined in the function invocation's local scope by this assignment
    # this does not cause global x to become defined
    # also, if you manage to run f() in parallel, each invocation will have a different local x
    # or if you run a different function, its local vars will be completely separate
    x = 1
try:
    print(x)
except Exception as e:
    print(e, type(e)) # NameError

# If there was a global x defined, the local x would shadow it inside the function.
x = 1
def f():
    x = 3
    print(x) # local x; shadows global x
f()
print(x) # global x

# If global x is defined, and local x is not, you can access global x but not assign to it.
def f():
    print(x) # global x (since no local x defined)
f()

# This one is a bit tricky.
# If you assign a local x *anywhere* in function and try to access x before that, you'll
# get an UnboundLocalError.
# Since Python compiles the functions, it has to know which variables are global or local inside
# it before it runs.
def f():
    print(x)
    x = "this makes x local causing the above statement to be illegal"
try:
    f()
except Exception as e:
    print(e, type(e))

# If you want to assign to global x inside your function, declare it global right at the start.
x = "global x before function call"
def f():
    global x
    print(x)
    x = "x was declared global from the start so the above line is legal"
f()
print(x) # will have been modified by the function call


# Parameters get turned into local variables. So, they shadow globals.
x = "global x before function call"
def f(x):
    print(x) # the parameter (a local variable)
    x = 13
f("argument")
print(x)

# You can't use a global declaration to cause a parameter to not be a local variable.
x = "global x before function call"
def f(x):
    # global x # NO: SyntaxError
    print(x)




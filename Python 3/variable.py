#!/usr/bin/env python3

# A variable is a named object reference.
# It does not hold the object itself, just a reference to it.
# It's like a pointer in other languages, but not statically typed. Can refer to anything.

# Have the name x in the current module/namespace refer to an integer with value 1.
# Assign object created from literal 1 to name x in the __main__ module (if running this file as a
# script).
# If importing this as a module, x is variable.x.
# A variable springs into existence as soon as you assign to it. No need to declare it in advance.
x = 1

# A script doesn't automatically have access to __main__ explicitly, but you can import it.
import __main__
__main__.x = 2

# You can see that x and __main__.x are really the same name.
print(x)

# See what names are bound/assigned in current namespace.
variables = dir()
print(variables)

# A variable can point to any kind of object.
x = 2.3 # float
x = [1, 2, 3] # list
x = "a string" # string

# You can delete a variable. Causes it to no longer exist.
del x

# You get a NameError if you try to access a variable that does not exist.
try:
    print(x)
except NameError as e:
    print("You tried to use variable x after it was deleted. It does not currently exist.")

x = 2 # x exists again
print(x)


# Variable names.
# Letters, numbers, and underscores. Nothing else. Can't start with a number.
# Can't be a reserved keyword.

# Can use this string method to check. Doesn't check vs. keywords though.
s = "valid_variable_name"
s.isidentifier()

import keyword
keyword.iskeyword(s)

# When you want to use a keyword for a variable name but can't, just add a trailing _.
class_ = None
in_ = None

snake_case_var = None # Recommend style for most things.
camelCaseVar = None
UpperCamelCase = None # Mainly used for class names.
var_with_numbers123 = None
__dunder_var__ = None # Legal, but you should avoid since many have special meanings in Python.
_start_with_underscore = None
_ = None # Yup, legal. This gets magically assigned to last expression value when running python interactive mode.

# 123var = None # NO: Can't start with a number.

ALL_CAPS = None # Fine. Often used for things intended to be constants.
l = None # Legal, but confusing. Better to use L or another letter.

# You can use some non-ASCII Unicode letters in variable names too.

# Variable names are case sensitive.
var = None
VAR = None # No problem.
vaR = None # Weird, but legal.

# When you do a function or class definition, it gets implicitly assigned to a variable.
def foo(): pass
foo = None # You can do this, but you've now lost access to the function.
try:
    foo() # Won't work. NoneType isn't callable.
except Exception as e:
    print(e, type(e))

# You can check if an object is callable before trying to call it.
if callable(foo):
    foo()
else:
    print("foo is not callable.")





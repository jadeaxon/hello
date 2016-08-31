#!/usr/bin/env python

# def function_name(param0, param1, ..., paramN):
#   block
#
# A function can have zero or more parameters.
# A function can return nothing or anything (including a list of things).
# A function without a return statement returns the value None, which is like null in Java.
#
# Arguments are passed using call by value (where the value is always an object reference, not the value of the object).
# Apparently, there are no primitives in Python, just object references.
#
# Functions appear to be first class objects.  You can store them in variables.
def fibonacci_function(n):   
    """Prints the Fibonacci series up to and including n.""" # This is like a Javadoc comment.
    a, b = 0, 1 # Multiple assignments on one line.
    while a <= n:
        print a, # Trailing print with a comma causes a newline not to be printed.
        a, b = b, a + b
    print

aGlobal = "I am a global variable."
def access_global():
    # You must declare global variables to access them within your function.
    global aGlobal
    print aGlobal


# Demonstrates returning a value from a function.
def fibonacci_function2(n):
    """Returns a list containing the Fibonacci series up to and including n."""
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a) # A method call on the list object.
        a, b = b, a + b
    
    return result


# You can assign default values to function parameters.  This lets you call the function with less arguments.
# You can use special * arguments to get all args as a list and/or a dictionary (hash/map).
# This might be a Python 2.7 feature.  It does not appear to be working correctly.
#
# Actually, what the two * parameters do is suck up all extra positional and named arguments respectively that are not
# specified in the formal parameter list.  This lets you make vararg functions with an unknown number of positional and/or
# named arguments.  Very flexible indeed.
def function_with_defaults(param1 = "foo", param2 = "bar", param3 = "baz", *extra_positional_args, **extra_named_args):
    print param1, param2, param3
    print extra_positional_args
    print extra_named_args



fibonacci_function(987)
access_global()

# Call a function via a reference to it.
function_ref = fibonacci_function
function_ref(2000)
series = fibonacci_function2(3000)
print series

function_with_defaults()
function_with_defaults("custom")
function_with_defaults("fee", "fi", "foe", "extra", "extra", extra="named")

# You can use param_name = value syntax to call a function.  Nice!
function_with_defaults(param3 = "fred")

# You can mix positional args with named args as long as you aren't ambiguous.  All positional args must come first though.
function_with_defaults("gold", param3 = "fever")


# To use a list to supply args to a function, prefix it with a *.
args = ["qux", "quux", "quuux"]
f = function_with_defaults
f(*args)

# To use a dictionary (hash) to supply arguments, prefix it with **.
args = {"param1": "eeny", "param2": "meeny", "param3": "miney"}
f(**args)



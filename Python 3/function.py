#!/usr/bin/env python3

def f():
    print("Hello, functions!")

f()

# Functions are objects.
g = f
g()
f.function_attribute = "This is a function"
L = [f, g]

# Functions can be dynamically defined at runtime.
if g is f:
    def g():
        print("Different function.")
g()

# You can use function attributes like static vars from C++.
def f():
    # Can access f before fully defined (else recursion would not work).
    if not hasattr(f, 'invocations'): f.invocations = 0
    f.invocations += 1
f()
f()
print(f.invocations)

# A function can have parameters.
# The actual values assigned to the parameters in a function invocation are that invocation's
# argumetns.
def f(x, y):
    print("arguments:", x, y)
f(2, 3)
f(3, 4)

# You can assign default values to parameters.
# Once you've assigned a default value, all subsequent parameters must have default values.
def f(x=0, y=0):
    print("arguments:", x, y)
f()
f(1)
f(1, 2)

# You can use the parameter names (in any order) when calling a function.
f(y=2, x=1)

# But, if there is a / in the parameter list, preceding params can only be provided args
# positionally.
def f(x, /, y):
    print("arguments:", x, y)
# f(x=1, y=2) # NO: TypeError: x is positional-only.
f(1, y=2)

# A function returns a value. By default, it returns None.
def f(x):
    return x * 2
value = f(3)
print(value)

# Function calls can happen just about anywhere since they are expressions.
L = [f(0), f(1), f(2) + f(3), f(f(4))]
print(L)

# You can create anonymous functions, lambdas.
# map() applies a function to all values in an iterable.
# It returns an iterator, so use list() to extract all the values.
iterator = map(lambda x: x * 2, L)
print(list(iterator))
f = lambda x, y: x + y # The anonymous function is no longer anonymous.
r = f(1, 1)
print(r)

# You can unpack iterable elements as positional function args.
args = [2, 2]
r = f(*args) # Same as f(2, 2)
print(r)

# You can unpack args from a dictionary too. As keyword args.
args = {'x': 2, 'y': 2}
r = f(**args) # Same as f(x=2, y=2)
print(r)

# Factory functions via closures.
# When you define a function inside another function, it saves a copy of all the parent/factory
# function's current local variable values with it (a closure).
def adder_factory(x):
	def adder(y):
        # Current value of x will be used in calls to adder() via closure.
		return y + x
	return adder

f = adder_factory(3)
g = adder_factory(2)
r = f(4) # 4 + 3 = 7
print(r)
r = g(4) # 4 + 2 = 6
print(r)

# Variadic function using positional args.
def f(*args):
    print(args) # args is a tuple of all arguments passed to function.
f(1, 2, 3, 4, 5, 6)

# Variadic function using keyword args.
def f(**kwargs):
    print(kwargs) # Everything in a dictionary.
f(foo=1, bar=2, baz=3)

# Variadic function with positional and keyword args.
def f(*args, **kwargs):
    print(args)
    print(kwargs)
f(6, 7, 8, qux='9')







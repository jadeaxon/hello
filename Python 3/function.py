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

# A function is a mechanism for code reuse.
# Here's a more flexible/reusable hello world.
def greet(salutation, greetee):
    print(f"{salutation.capitalize()}, {greetee}!")

greet("Hello", "world")
greet("Yo", "Adrian")
greet("Good morning", "Vietnam")
greet("Howdy", "pilgrim")

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

# A function returns a value (any expression). By default, it returns None.
# The function exits immediately when it hits a return.
# It returns a value to wherever it was called from and resumes execution there.
def f(x):
    if x >= 0:
        return x * 2 # returns the value of any expression
    return # returns None if used by itself
    # If function ends without hitting a return, it returns None
value = f(3)
print(value)

# Function calls can happen just about anywhere since they are expressions.
# For nested calls, the innermost function calls will happen first.
# When used with operators, precedence and the binding order will determine which function is
# called.
# When used in an argument list, the function calls will happen left to right.
L = [f(0), f(1), f(2) + f(3), f(f(4))]
print(L)

# You can call a function that returns a value other than None without assigning its result.
# Since the object it returns isn't referenced by any variable, it will just be garbage collected.
# Functions are often called solely for their side effects, not their return value:
# print(), functions that mutate a list in-place, functions that alter files, etc.
f(7)

# You can pass a list to a function.
# While the list reference is passed by value, you'll still be pointing to the same list object.
# Thus, you can mutate it.
# Same idea applies to any mutable object.
# If you don't want to change the original list, pass a copy of it using L[:] or L.copy()
print("Mutating a list.")
L = [1, 2, 3]
def mutate_list(list_):
    # list_ is pointing to the same list the caller passed.
    list_.clear()
    list_ = None # This does not affect what global L is assigned to: list_ (the ref/var/name) is a copy of L.
mutate_list(L)
print(L) # L is now empty. The function wasn't passed a copy of L. Just a copy of a reference to L.

# You can return lists (and other more complex objects) from a function.
def create_list():
    list_ = []
    list_.append("foo")
    list_.append("bar")
    return list_
L = create_list()
print(L)

# You can create anonymous functions, lambdas.
# map() applies a function to all values in an iterable.
# It returns an iterator, so use list() to extract all the values.
L = [1, 2, 3, 4]
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


# A weird example of where Python does not quite execute line by line.
x = 13
def f():
    y = 0
    # y = x + 1 # Should work. Using an unshadowed global in an expression.
    # NOPE: You get UnboardLocalError because x is assigned to *later* in the function.
    # Functions still get compiled at runtime.
    # Python has to decide at the start of the function which vars are local and global.
    print(y)

    x = 1 # Should work. Assigning to x should turn it into a local variable.
    y = x + 1
    print(y)

    # global x # Should work. We're saying x is really global x from here on out.
    # NOPE: Python isn't that dynamic. Says x is used before global declaration.
    y = x + 1
    print(x)
f()




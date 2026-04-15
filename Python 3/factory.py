#!/usr/bin/env python3

# A factory function returns other functions.
# Works since it gets a closure of the enclosing local variables at time of creation.
def create_function(x):
    def adder(y):
        # Will use the enclosed value of x whenever called.
        return y + x
    return adder

f = create_function(2)
r = f(3) # 3 + 2
print(r)
g = create_function(4)
r = g(3) # 3 + 4
print(r)

# A class acts like an object factory. When you call it via (), you get a new class instance.
class Foo(): pass
instance = Foo()
instance2 = Foo()
instance is instance2 # False

# You can even make functions that return classes.
# Even though the classes are local vars, they don't go away when you return a ref to them.
# The problem with this implementation is that a new Holiday or Day class will be created
# each time you call the function. This may or may not be what you want.
def create_class():
    is_holiday = True
    if is_holiday:
        class Holiday(): pass
        c = Holiday
    else:
        class Day(): pass
        c = Day
    return c

class_ = create_class()
print(class_)
instance = class_()
print(instance)



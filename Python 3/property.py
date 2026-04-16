#!/usr/bin/env python3

# Making x a property lets us access it with o.x, o.x = v, and del o.x instead of
# using method calls like o.getX(), o.getX(v), and o.deleteX().
class Foo():
    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        print("Using getter.")
        return self.__x

    @x.setter
    def x(self, value):
        print("Using setter.")
        self.__x = value

    @x.deleter
    def x(self):
        print("Using deleter.")
        del self.__x

o = Foo()
# This actually doesn't work since __ names get mangled. It becomes _Foo__x.
# print(o.__x)
print(o._Foo__x)
print(dir(o))
o.x = 1
print(o.x)
del o.x
print(o._Foo__x) # Exception



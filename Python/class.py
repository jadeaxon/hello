#!/usr/bin/env python

# Classes are created dynamically at runtime.
# They create a class object.
# Defining a class creates a new namespace within the innermost enclosing namespace.
# A namespace is essentially just a hash that maps a name to an object.
#
# All methods in Python are virtual.  That is, they behave polymorphically.
#
# Python supports multiple inheritance.


class BaseClass:
    pass


# Greeter inherits from BaseClass.
class Greeter(BaseClass):
    """A simple example class."""

    # It is a good idea to prefix attributes you with to be private with an underscore.
    # Generally, client code should not access any data attributes directly.  Client code should use only public methods (the interface).
    _identity = 12345

    
    # The constructor is called __init__
    def __init__(self):
        self.data = []

    # Unlike in Java 'this' is not implictitly passed to methods.
    # In Python, the first param acts as 'this' and is called 'self' by convention.
    def say_hi(self):
        print 'Hello, world!'
        print 'I am an instance of class ' + str(self.__class__) + '.'


    # An example of supporting iteration.  No good for multiple threads.
    def __iter__(self):
        self.greetings = 10
        return self
                
    def next(self):
        if self.greetings == 0:
            raise StopIteration
        
        self.greetings -= 1
        return "Greetings!"

        

# The class is actually itself an object.
print Greeter

# Instantiate a new instance of the class.
instance = Greeter()
print instance
print

# Invoke a method on the instance.
# instance.method() => Class.method(instance)
instance.say_hi()

# A method is just a function object.  You can assign it to a variable and call it later.
# Methods bind the instance to the call.
method = instance.say_hi
method()
print

# Python has some built in predicates for checking class membership and inheritance relationships.
if isinstance(instance, Greeter):
    print "'instance' is an instance of class Greeter."

if issubclass(Greeter, BaseClass):
    print "Greeter is a subclass of BaseClass."
print

# Use instance in a for loop since it implements iterable interface.
for greeting in instance:
    print greeting
print





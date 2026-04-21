#!/usr/bin/env python3

# Define a new class using explicit base class.
class Thing(object): pass

# object is the default base class, so you can omit it
class Thing(): pass

# You can also omit the ()s in this case.
# Like functions, classes do an implicit assignment to their name.
# So, the last class definition for the same name will be active.
class Thing: pass

# Create an instance of the Thing class.
# This works because Python automatically adds a zero-arg __init__() method to a class.
# A class itself is an object.
if isinstance(Thing, object):
    print("The Thing class is itself an object.")
if callable(Thing):
    print("You can call the Thing class like a function.")

# When you call a class, you construct a new instance of the class.
# Under the hook, the constructor __new__ is called. Then the initializer __init__ is called.
o = Thing()

# A user-define class also gets a default __str__ method so it can be printed as a string.
print(o, type(o))

# Can't do much with Thing, so lets give it attributes and methods.
# Note that class names are usually CamelCase.
class Thing:
    # A class itself can have attributes.
    # This would be information about the class itself.
    # Or an attribute that all instances of the class have in common.
    description = "A class of things that can grow new limbs and attack."
    disgusting = True

    # Overwrite the default __init__ method.
    # Be aware that you can only have one curretly defined __init__ method.
    # There is no method signature overloading like in other languages.
    # You have to pass the special self arg to all instance methods as first arg.
    # This represents the object itself. It is like 'this' in other languages.
    # Technically, you don't have to name it 'self', but it is a strong convention to do so.
    def __init__(self, name, limbs):
        self.name = name
        self.limbs = limbs

    def attack(self):
        print(f"{self.name} attacks with {self.limbs} limbs.")

    # Note that method names are usually snake_case.
    def grow_limb(self):
        self.limbs += 1
        print(f"{self.name} grows yet another limb!")

    # Override default __str__.
    # This gets called by str() and print() to convert an object to a string.
    def __str__(self):
        s = f"A Thing named {self.name} with {self.limbs} limbs."
        return s

# Access a class attribute.
print(Thing.description)

# Create a Thing and have it do something.
o = Thing("Gribnob", 3)
o.attack()
o.grow_limb()
o.attack()
print(o) # Uses our custom __str__

# All attributes are public, so you can access them directly.
# Having an attribute start with __ mangles its name to make it sort of private.
print(f"I can see that {o.name} has {o.limbs} limbs.")

# You can assign to attributes directly, delete them, and add new ones.
# An object acts like its own mini module/namespace.
o.eyes = 3
print(f"{o.name} now has {o.eyes} eyes.")
o.limbs = 7
o.attack()
del o.eyes

o2 = Thing("Blurbnog", 4)

# You can access class attributes by class instances (if not shadowed by an instance attribute).
if o.disgusting:
    print(f"Yup, {o.name} is kind of disgusting.")
if o2.disgusting:
    print(f"Indeed, {o2.name} is also quite disgusting.")

class ClonableThing(Thing):
    def __init__(self, name, limbs):
        super().__init__(name, limbs) # Call the superclass initializer.
        self.clones = 0

    def clone(self):
        # No conflict since the clone method is self.clone.
        print(f"We're doomed! {self.name} has cloned itself!")
        self.clones += 1
        clones = self.clones
        name = self.name
        if name.startswith("Clone"):
            name = "c" + name[1:] # In case we have clones of clones.
        name = f"Clone {clones} of {name}"
        clone = ClonableThing(name, self.limbs)
        return clone

o3 = ClonableThing("Zigmort", 2)
o4 = o3.clone()
o4.attack()
o5 = o4.clone() # This is getting out of control!
o5.attack()
o6 = o3.clone()
o6.attack()

# Let's make some of those semi-private attributes.
class ShyThing(Thing):
    def __init__(self, name, limbs):
        super().__init__(name, limbs)
        self.__secret = f'my secret is {id(self)}'

    def tell_secret(self):
        # Inside the class, you can use the unmangled name.
        # Outside the class, you can't.
        secret = self.__secret
        if self.__not_feeling_shy():
            print(secret)
        else:
            print("No!")

    def tell_secret_or_else(self):
        print("Fine!")
        print(self.__secret)

    # The __ semi-private name mangling works for methods too.
    # You can use this for private helper methods that shouldn't be part of the class's public interface.
    def __not_feeling_shy(self):
        return False

o = ShyThing("Wallflower", 1)
o.tell_secret()
try:
    print(o.__secret)
except AttributeError:
    # For variables, we get a NameError when trying to access undefined things.
    # For object attributes, we get an AttributeError instead.
    print("Hmmm, how do we find out the secret?")

# __secret actually gets mangled into _<class>_<attribute>; _ShyThing__secret in this case
print(o._ShyThing__secret) # Aha!
o.tell_secret_or_else() # Threaten the object








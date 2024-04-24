# Classes.
# Dictionaries that store functions that act on the dictionary data, more or less.

# Python uses PATH to search for modules. Classes are defined in modules.
import os, sys
file_dir = os.path.dirname(__file__)
if file_dir not in sys.path:
    sys.path.append(file_dir)

# Import the Dog class from the dog module.
from dog import Dog # type: ignore
from dog import Warg # type: ignore

my_dog = Dog('Fido', 3) # Create a Dog instance.
print(f"My dog's name is {my_dog.name}.") # Directly access an attribute.
my_dog.sit() # Call an instance method.
my_dog.roll_over()

# You can create multiple instances of a class.
your_dog = Dog('Spot', 6)
your_dog.sit()
your_dog.roll_over()

# Warg inherits from Dog.
a_warg = Warg('Fang', 2)
a_warg.attack() # The warg has methods (and attributes) a dog does not.
a_warg.sit() # But it can still do what dogs do.
a_warg.roll_over() # It may do things differently than its parent class though (via overriding methods).






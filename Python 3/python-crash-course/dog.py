class Dog:
    """ A simple class representing a dog. """

    # Initializer.
    def __init__(self, name, age):
        """ Initialize dog instance. """
        self.name = name
        self.age = age
        # name and age are now attributes of this Dog instance.
        
    # An instance method.
    # Note that you have to pass self as first arg.
    def sit(self):
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        print(f'{self.name} rolls over.')

# Use inheritance.
# The Warg can do anything a Dog can do, but it can do more.
class Warg(Dog):
    def __init__(self, name, age):
        # Call the superclass constructor.
        # super() lets you call any method of the parent class (the superclass).
        super().__init__(name, age)
        self.rage = 0 # Add a new subclass method.

    def attack(self):
        print(f"Warg {self.name} attacks!")
        self.rage += 1

    # Override a parent class method.
    def roll_over(self):
        print("The warg growls at you. It does not do silly tricks.")

        





    

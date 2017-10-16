#!/usr/bin/env python3

# Superclass.
class Parent(object):
    def __init__(self):
        self.id = "1"

    # This will be overriden by subclass.
    def override(self):
        print("PARENT override()")

    # This will not be overriden by subclass.
    # However, subclass can still call it because inherited.
    def implicit(self):
        print("PARENT implicit()")

    # This is overriden, but the override relies on calling
    # this superclass version of the method.
    def altered(self):
        print("PARENT altered()")

# Subclass.
class Child(Parent):
    def __init__(self, name):
        super(Child, self).__init__()
        self.name = name

    # Completely override superclass method.
    def override(self):
        print("CHILD override()")

    # Override superclass method, but implement it in terms
    # of the superclass method.
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # Call the superclass method. 
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

class Other(object):
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

# Use composition rather than inheritance.
class Youngling(object):
    def __init__(self):
        self.other = Other() # Delegate to this object.

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("YOUNGLING override()")

    def altered(self):
        print("YOUNGLING, BEFORE OTHER altered()")
        self.other.altered()
        print("YOUNGLING, AFTER OTHER altered()")

# daughter = Youngling("Rosemary's Baby")
daughter = Youngling()
daughter.implicit()
daughter.override()
daughter.altered()

# Instantiate objects.
dad = Parent()
son = Child("George Foreman Jr.")

# Call non-overriden method.
dad.implicit()
son.implicit()

# Call the pure override.
dad.override()
son.override()

# Call the override that uses a superclass call.
dad.altered()
son.altered()




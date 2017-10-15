#!/usr/bin/env python3

## Animal is a object (yes, sort of confusing). 
# Look at the extra credit.

class Animal(object):
    def eat(self, food):
        print(f"Animal::eat({food})")

## Dog is a Animal.
class Dog(Animal):
    def __init__(self, name):
        ## This Dog has a name.
        self.name = name

    def eat(self, food):
        print(f"Dog::eat({food})")

## Cat is a Animal.
class Cat(Animal):
    def __init__(self, name):
        ## A Cat instance has a name.
        self.name = name

    def scratch(self, foe):
        print(f"This cat scratches foe {foe}.")

## A Person is an object.  Why didn't Python call it Object?
# Maybe all keywords are lowercase?
class Person(object):
    def __init__(self, name):
        ## A Person has a name.
        self.name = name

        ## A Person may have a pet.
        self.pet = None
        self.children = []

    def greet(self):
        print(f"Hello, I am {self.name}!")

    def have_child(self, name):
        child = Person(name)
        self.children.append(child)

## An Employee is a Person.  Although you couldn't tell that based on
# the behavior of some companies.
# 'self' isn't supposed to be special, so I changed it to 'serf' in this context.
class Employee(Person):
    def __init__(serf, name, salary):
        ## Superclass constructor chaining.
        super(Employee, serf).__init__(name)
        ## An Employee has a salary.
        serf.salary = salary

    def quit(serf):
        if serf.salary >= 100000:
            print("Thanks for all the fish.")
        else: # Not paid enough.
            print("Screw this job!")

## A Fish is an object.
class Fish(object):
    def swim(self):
        print("Glub glub glub.")

## A Salmon is a Fish.
class Salmon(Fish):
    def swim(self):
        print("Swish swish swish.")

## A Halibut is a Fish.
class Halibut(Fish):
    def swim(self):
        print("Hibble hibble hibble.")

thing = Animal()
thing.eat("gruel")

## Rover is a Dog.
rover = Dog("Rover")
rover.eat("bacon")

## Satan is a Cat.
satan = Cat("Satan")
satan.eat("tuna")
satan.scratch("Rover")

## Mary is a Person.
mary = Person("Mary")
mary.greet()
mary.have_child("Jimmy")
mary.have_child("Becky")
print(mary)
print(mary.children)

## Mary has a pet Cat, satan.
mary.pet = satan
mary.pet.scratch("Mary")

# Frank is an Employee.
frank = Employee("Frank", 90000)
frank.quit()

# Frank has a pet: Rover.
frank.pet = rover

## Flipper is a Fish.
flipper = Fish()
flipper.swim()

## Crouse is a Salmon.
crouse = Salmon()
crouse.swim()

## Harry is a Halibut.
harry = Halibut()
harry.swim()





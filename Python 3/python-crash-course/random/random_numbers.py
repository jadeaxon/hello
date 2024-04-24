# Random numbers.

# The random module is part of the Python standard library.
# Huh, if you try to import a module into a file with the same name, Python chokes.
# Guess I can't call this file random.py.
# Well, it is if you have any file in the same directory named after a core Python module.
# Moving this to a subdir got past the circular import error.
from random import randint # Generate a random integer.
from random import choice # Randomly choose from a list.
from random import shuffle # Randomly shuffle a list.
from random import sample # Take a random sample of size n from a list/collection.

values = ['foo', 'bar', 'baz', 'qux']

while True:
    number = randint(1, 6) # Random int between 1 and 6 inclusive.
    value = choice(values) # Randomly choose form a list of values.
    shuffle(values) # Shuffle the list.
    print(number)
    print(value)
    print(values)
    input("Hit enter to roll again.")




#!/usr/bin/env python3

# This file acts as a module and a script.

# Everything in the file runs on first import.
# For 'import mystuff' each symbol defined in this file becomes
# accessible as mystuff.<symbol> in the importing file.

print("Loading module mystuff.")
# This can be accessed via mystuff.mystuff in importing file.
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# mystuff.apple()
def apple():
    print("I AM apple()!")

# mystuff.pear()
def pear():
    print("I AM pear()!")


# You can also define classes in a module.
class Fruit:
    def __init__(self):
        print("Creating a Fruit instance.")

# A module can have plain vars too.
tangerine = "Living reflection of a dream"

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    def apple(self):
        print("I AM CLASSY APPLE!")



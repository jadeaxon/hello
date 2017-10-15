#!/usr/bin/env python3

# Use the other file as a module.
# What happens is when we run this script, we're in a namespace
# called __main__.  The import statement causes the mystuff module
# to be loaded (as an object) and then assigned to __main__.mystuff.
# We could use 'as' to give it a different name in this namespace.

# What happens if you import the same module twice?
# Seems to just work.  Notice that the extraneous code at beginning
# of module DOES run.
import mystuff
# This appears to only reassign the name.  The init code does not run
# again.
import mystuff as my
from mystuff import Fruit as Fruit
from mystuff import MyStuff as MyStuff

my.apple()
my.pear()
print(my.mystuff)

f = Fruit() # Instantiate a Fruit.

print(my.tangerine)

m = MyStuff()
m.apple()
print(m.tangerine)

print(my.mystuff['apple'])

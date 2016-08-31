#!/usr/bin/env python

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots', 'bananas', 'peaches']
change = [1, 'pennies', 2, 'nickles', 3, 'dimes', 4, 'quarters']

# This first kind of for loop goes through a list.
for number in the_count:
    print "This is count %d." % number

# Same idea again.
for fruit in fruits:
    print "A fruit of type: %s" % fruit


# Also, we can go through mixed lists since Python uses dynamic typing.
# Notice how we have to use %r since we don't know what type the element holds.
for element in change:
    print "I got %r." % element

# We can also build lists.  Let's start with an empty list.
elements = []

# Now, use the range function.
for i in range(0, 6): # 0 .. 5
    print "Adding %d to the list." % i
    elements.append(i) # 'append' is a method applicable to lists.

# Now we can print them out.
for i in elements:
    print "Element is %d." % i




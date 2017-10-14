#!/usr/bin/env python3

# Assign a var to a list literal.
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
# Note that a list can contain mixed types.
# Python is dynamically typed.
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for loop goes thru a list.
# For (each) element in list.
for number in the_count:
    print(f"This is count {number}.")

# Same as above.
for fruit in fruits:
    print(f"A fruit of type {fruit}.")

# Also, we can go through mixed lists.
for i in change:
    print(f"I got {i}.")

# We can also build lists.  Start with an empty list.
elements = []

# Then use the range function to generate numbers.
# The max bound is not inclusive.
for i in range(0, 6): # 0..5
    print(f"Adding {i} to the list.")
    # Append is a list method.
    elements.append(i)
    # Could probably do elements += i.

# Faster than above.
elements = range(0, 6)

# Now we can print out all the elements of the list.
for e in elements:
    print(f"Element: {e}.")



#!/usr/bin/env python3

# A simple function.
def my_function(x, y):
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"x + y = {x + y}")
    print("----") 
    x = 0
    y = 0
    return 1

# Variables of the same name as the function locals.
# Let's see if they mutate.
x = 1
y = 2

# Call my function in 10 different ways.
my_function(2, 3)
my_function(1 + 1, 2 + 2)
my_function(my_function(2, 3), my_function(4, 5))
my_function(x, y)
my_function(x + 1, y + 1)
my_function(len("one"), len("three"))
my_function(y, x)
my_function(x=4, y=5)
my_function(3.2, 7.9)
print(f"{my_function(7, 8)}")
print(f"global x = {x}; global y = {y}")



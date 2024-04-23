# Functions.
# Named, parameterized, reusable blocks of code.

# Define a function.
def hello():
    """ Say hello. """
    # The line above is a docstring.
    print("Hello!")

# Looks like you cannot overload functions.
# def hello(user):
def hello2(user):
    """ Say hello to a specific user. """
    print(f"Hello, {user}!")

# Each parameter can have a default value.
# All parameters with default values have to come after those that have no default value.
def hello3(user='default user'):
    print(f"Hello, {user}!")

# A function can have multiple positional parameters.
# A function can return a value. It can be a complex value like a dictionary.
def add(x, y):
    result = x + y
    return result

# When you pass a list into a function, you can modify the list. It is not a copy.
# If you don't want to modify the original list, use list[:] to copy the list.
# A list slice that contains the entire source list.
def process_list(list):
    while list:
        element = list.pop()
        print(f'Processing {element}.')
        
# Call the functions.
hello()
hello2("programmer")
hello3() # Rely on default parameter value.

sum = add(7, 9)
print(sum)

process_list([3, 7, 9])
list = [5, 6, 7]
process_list(list[:]) # Pass a copy.
print(list) # Should not be empty.

# A function can also be called using keyword arguments (named parameters).
# Note that they can be in a different order than positional args would need to be.
sum = add(y=20, x=10)
print(sum)


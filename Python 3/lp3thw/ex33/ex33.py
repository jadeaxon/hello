#!/usr/bin/env python3


# Move the globals to be local vars.

# Returns a list of 0..bound-1.
# Works like the range() builtin.
# PRE: step is positive
def loopy(bound, step=1):
    # Init vars.
    numbers = []
    i = 0
    # Loop until i is 6 or greater.
    while i < bound:
        print(f"At the top i is {i}.")
        numbers.append(i)
        # Increment control var so loop exits eventually.
        i += step
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}.")
    return numbers

def ranger(bound, step=1):
    numbers = []
    for i in range(0, bound, step):
        print(f"At the top i is {i}.")
        numbers.append(i)
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}.")
    return numbers 

# Call function we made to wrap the loop.
# numbers = loopy(8, 2)
numbers = ranger(8, 2)

# Print the results.
print("The numbers:")
for num in numbers:
    print(num)



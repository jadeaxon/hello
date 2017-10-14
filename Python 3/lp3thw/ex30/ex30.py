#!/usr/bin/env python3

# Assign values.
people = 30
cars = 20
trucks = 25
toggle = False

# Do if block if more cars than people.
if cars > people:
    print("We should take the cars.")
# Do else if block if above false and cars less than people.
elif cars < people:
    print("We should not take the cars.")
# Do else block if all preceding conditions fail.
else:
    print("We can't decide.")

# If more trucks than cans and toggle set, do if block.
if (trucks > cars) and toggle:
    print("That's too many trucks.")
# If if condition false and less trucks than cars, do else if block.
elif trucks < cars:
    print("Maybe we could take the trucks.")
# If all above conditions are false, do the else block.
else:
    print("We still can't decide.")

# Test boolean expression.  Execute just the following block if true.
if (people > trucks) or (people != cars):
    print("Alright, let's just take the trucks.")
# Execute this block if the if expression evaluates to False.
else:
    print("Fine, let's stay home then.")



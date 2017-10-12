#!/usr/bin/env python3

# Define a simple function that takes two args.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Call function with hard-coded values (literals).
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
print("Or, we can use variables.")
# The point is that the args are passed by value.
# So, changes in the function scope do not affect vars in the callers scope.
amount_of_cheese = 10
amount_of_crackers = 50

# Call function with variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call function using expressions as args.
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Mix it up.
print("And we can combine the two: variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#!/usr/bin/env python3

# if statement
# conditionally executes code

# The if condition can be any expression.
# Its boolean value will be determined.
# If the expression evaluates to True, run the if block.

x = "evaluates to true"
y = 10
z = 3
if True:
    print("True")
if 17:
    print(17)
if x:
    print(x)
if y > z:
    print("y > z")

# You can also have an else clause/block.
# It will run when the condition is false.
if False:
    print("this won't run")
else:
    print("the condition is false: run the else clause")
    print("each clause can have more than one statement in it")

# You can also do elif conditions.
# The if/elif conditions will be evaluated top to bottom.
# The clause of the first condition to evaluate as true will be run.
# The else clause will run if all the if/elif conditions evaluate as false.
if False:
    pass
elif []:
    pass
elif 0:
    pass
elif {}:
    pass
else:
    print("None of the above conditions were true.")

if False:
    pass
elif "evaluates as true":
    print("The first true clause will be run.")
elif True:
    print("This won't run.")
else:
    print("Neither will this.")






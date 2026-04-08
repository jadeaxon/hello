#!/usr/bin/env python3

# Loop from 0 to 4.
# If only one arg to range(), it is the stop.
# Stop is the first value to *not* be included in resulting list.
for i in range(5):
    print(i)
print()

# Loop from 1 to 5.
# If two args, the first is start. It is the first value to be included.
for i in range(1, 6):
    print(i)
print()

# A for loop can have an else clause.
# Always executes once (on loop exit).
for i in []:
    pass
else:
    print("for loop else")
print()

# Range can take a 3rd argument: the step.
# Even numbers between 0 and 10.
for i in range(0, 11, 2):
    print(i)
print()

# You can do ranges in reverse.
# The start and stop args preserve their meaning. Thus 10 will be the first included value.
for i in range(10, -1, -2):
    print(i)
print()

# Same thing using reversed() instead.
for i in reversed(range(0, 11, 2)):
    print(i)
print()




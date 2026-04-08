#!/usr/bin/env python3

from time import sleep

count = 5
while count > 0:
    print(count)
    count -= 1
print()

# You can use () if used to from other languages, but its optional.
# The walrus operator, :=, lets you assign counter in loop body since it returns a value.
# Note that it returns the value after assignment.
count = 3 + 1
while (count := count - 1):
    print(count)
print()

# A while loop can have an else clause.
# It always executes once (on loop exit).
while False:
    pass
else:
    print("while loop else")
print()

# Infinie loop. Press ^C to escape.
while True:
    print("Infinite loop. Press ^C to escape.")
    sleep(1)



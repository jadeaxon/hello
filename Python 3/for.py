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

# Remove all the vowels from a string.
# You can use 'continue' and 'break', but Python doesn't support labeled loops.
s = "Remove all the vowels."
s2 = ""
for c in s:
    if c.lower() in list("aeiou"): continue
    if c.lower() == 'y':
        print("Confused.")
        break
    s2 += c
print(s2)
print()

# If you need the indexes and elements when iterating over a list, use enumerate().
for i, v in enumerate(['one', 'two', 'three']):
    print(i, v)
print()

numbers = [2, 3, 4]
squared = [4, 9, 16]
cubed = [8, 27, 64]
# Loop over two or more sequences at once using zip().
for n, s, c in zip(numbers, squared, cubed):
    print(n, s, c)
print()



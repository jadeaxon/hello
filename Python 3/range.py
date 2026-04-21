#!/usr/bin/env python3

# range() returns an immutable iterable integer sequence that is lazily evaluated.
# But, what it returns is not a generator since you can iterate over it multiple times.
# It returns an instance of class range.

# range(start, stop, step)
# range(stop)

# The range of integers is from start (inclusive) to stop (exclusive) by steps of step.

# If called with one arg, that arg is used as stop.
r = range(3)
L = [i for i in r]  # [0, 1, 2]
print(L)

# A range can be iterated over more than once.
L = [i + 1 for i in r] # [1, 2, 3]
print(L)

# If called with two args, they are start and stop.
r = range(1, 3)
L = [i for i in r]  # [1, 2]
print(L)

# If called with three args, they are start, stop, step.
r = range(1, 10, 2)
L = [i for i in r]  # [1, 3, 5, 7, 9]
print(L)

# The step can be negative. Make sure you flip your start/stop values.
r = range(9, 0, -2)
L = [i for i in r]  # [9, 7, 5, 3, 1]
print(L)

# Since a range is a sequence, it can be sliced.
r = range(20)
r2 = r[::-1] # reverse
L = list(r2)
print(L)




#!/usr/bin/env python

# while <boolean expression>:
#   block

# As long as <boolean expression> is true, block gets executed.

# An infinite loop.  Sort of.
count = 1
while True:
    count += 1
    if count >= 10000:
        print "Reached the end."
        break # Explicitly exit the innermost loop.




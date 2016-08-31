#!/usr/bin/env python

# 'True' and 'False' are Python's boolean literals.  I like the lowercase ones in Java better.

# A simple if statement.
if True:
    print "The boolean expression evaluates to true.  Execution branches to this statement."


# An else if switch.
# Python uses indentation as part of the syntax to identify blocks.
#
# Each if and elif requires a boolean expression.  The expression does not have to be in parenthesis.
# Note how each line preceding a block is ended with a colon.
x = 42
if x < 0:
    x = 0
    print 'Negative changed to zero'

elif x == 0:
    print 'Zero'

elif x == 1:
    print 'One'

else:
    print 'Many'



#!/usr/bin/env python

i = 0
numbers = []

while i < 6:
    print "At the top, i is %d." % i
    numbers.append(i)

    # i++ -- Are you joking?  No ++ operator!!!
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom, i is %d" % i

print "The numbers: "

for number in numbers:
    print number



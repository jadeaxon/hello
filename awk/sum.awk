#!/usr/bin/awk -f

# Expects a stream of numbers, one per line.
# Outputs the sum.

# BEGIN { print "Adding numbers." }

# If you refer to a variable that DNE yet, awk simply creates it.
# { sum = sum + $0 }
# { sum=sum + $1 }

# You can use the C shortcut operators.
{ sum += $0 }

# You can dereference the variable (get its value) using $<variabl> syntax.
# Actually, this is a lie.  Variables do not expand inside strings like they do in Perl.
# This is probably one of the reasons Perl was invented.
# END { print "$sum" }

# You use them like this:
END { print sum }




#!/usr/bin/env python

string = "This is a string."

s2 = 'This is also a string.'

s3 = r'This is a raw quoted string.  A \n does not escape to a newline.'

s4 = "A string can be continued \
across multiple lines \
by backslashing the end of the previous line.\
"
# Notice how using the line continuation \ with the doc string lets me format it nicely
# within the code.  The string has no extra or trailing newline.
docstring = """\
This is a doc string.
It continues over multiple lines.
It's good for holding larger chunks of text like paragraphs.\
"""

docstring2 = '''\
You can also use single quotes for a doc string.
The quoting is the same as in single quoted strings.
Perl calls these things here documents.
Perl's quoting mechanisms are stronger than Python's.\
'''

help_message = """\
Usage: hello_string.py

This command demonstrates basic string usage in Python.  It starts out by
showing some useful quoting mechanisms for creating string literals.  It then
shows interpolating variable values into strings and printing them to stdout.
After that, it shows some useful string manipulation functions.

Author: Jeff Anderson\
"""

concatenation = "You can concatenate " + "two strings with the + operator."

padded = "    There was extra whitespace to the left and to the right before I called strip().   \n"
stripped = padded.strip()
rstripped = padded.rstrip() # Just strip whitespace from right.  Kind of like chomp in Perl. 

unicode_string = u'This is a Unicode string.'

print help_message
print
print string
print s2
print s3
print s4
print docstring
print docstring2
print concatenation
print stripped
print rstripped
print unicode_string
print

# Strings act like arrays of characters.
# Looks like you cannot assign to a string subscript.
# string[0] = "insert" # This is not legal.
# string[0] = 't' # Nor is this.
print string
print "len(string) => %s" % len(string) # Get the length of a string.
print "string[0] => " + string[0]
print "string[-1] => " + string[-1] + " (gets last element)."
print "string[-2] => " + string[-2]

# Any time the right index is greater than the left index, an empty string is returned.
print "string[-1:0] => " + string[-1:0] # Not the string reversed as you might guess.

# You can get string slices.
# The range end is exclusive.  Substring length is exclusive end minus inclusive start.  Assuming step size of 1.
print "string[0:2] => " + string[0:2]
print "string[:2] => " + string[:2]
print "string[0:] => " + string[0:]
# If you use a too large index, Python will just substitute the largest legal value.
print "string[0:1000] => " + string[0:1000]
print "string[:] => " + string[:]
print "string[1:3] => " + string[1:3]
print "string[0::2] => " + string[0::2] + " (every other letter starting with first)"


number = 123
print "Convert a number to a string with str(): " + str(number)
print

# You can right justify, left justify, or center a string within a given width.
string = "move"
print '|' + string.rjust(10) + '|'
print '|' + string.ljust(10) + '|'
print '|' + string.center(10) + '|'

# zfill left pads a string with zeros.
print '|' + string.zfill(10) + '|'

# You can use the format method on a string to inject values.
# The format method is the more modern way to format strings.
#
# FAIL: formatted = 'We are the {} who say "{}!"'.format('knights', 'Ni')
# print formatted
formatted = 'We are the {1} who say "{0}!"'.format('knights', 'Ni')
print formatted

formatted = "This {food} is {adjective}!".format(food="hamburger", adjective="delicious")
print formatted

# The old style of string formatting uses the % operator and sprintf-like syntax.
# Alledgedly, this style will be removed from Python in the future.
formatted = "I will %s a value." % ('substitute')
print formatted

# Use the replace method to do a simple non-regexp search and replace.
print 'tea for too'.replace('too', 'two')



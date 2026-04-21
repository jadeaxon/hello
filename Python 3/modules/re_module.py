#!/usr/bin/env python3

"""
See Regular Expressions.txt
https://docs.python.org/3/library/re.html
"""

import re

s = "search me"

# Find the first match of the regular expression (pattern).
# match_object = re.search('<regex>', string_to_search)
match_object = re.search(" .*$", s)
print(match_object, type(match_object))
print(match_object.group(0)) # The actual substring matched.

# If there is no match, search() returns None.
mo = re.search("not found", "foo bar baz")
print(mo)

# Why do we get back a match object?
# First, you might want to know the location of the match.
# Second, if a regular expression has ()s it may capture multiple submatches (groups).
# You may want to look at those submatches.
# group 0 is what the entire regex matches.

# Get a list of all matches.
# Inconsistently, findall() does not return match objects.
# Returns an empty list if no matches found.
s = "search me; now search me again"
substrings = re.findall('search me', s)
for ss in substrings:
    print(ss)

# Split a string.
s = "split--me---up----Scotty"
pieces = re.split("-+", s)
print(pieces)

# Substitute matches with another substring.
# re.sub('<regex>', substitution, string_to_modify)
patched = re.sub("-+", "-patch-", s)
print(patched)

# Subgroups.
s = "nope foo bar baz nada"
mo = re.search(r'(f..) (b..).*?(n...)', s)
for group in mo.groups():
    print(group)







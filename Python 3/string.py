#!/usr/bin/env python3

s = "This is a string."
s = 'This is also a string.'
s = s + " With stuff appended." # + operator joins strings.
print(s)
t = type(s)
print(t)

s = "echo "
s = s * 3 # * operator repeats strings.
print(s)

x = 3
s = f"The value of x is {x}." # Use f-strings to interpolate variables inside strings.
print(s)

# Multiline string.
mls = \
"""
Multiline
string
"""
print(mls, end="")

# Multiline f-string.
fmls = \
f"""
The value of x is:
{x}
"""
print(fmls, end="")

#==============================================================================
# String Methods
#==============================================================================

s = "foo bar baz"
stabs = "tab\ttabby\ttabulous"

# Capitalize the first character.
s2 = s.capitalize()
print(s2)

# Returns a version of string that can be used in caseless comparison.
# Works better than just using lower() method when dealing with arbitrary Unicode.
s2 = s.casefold()
print(s2)

# Center a string within a given width field using a given padding character (defaults to space).
s2 = s.center(20, '_')
print(s2)

# Count non-overlapping instances of substring. Optional start and end args to limit search range.
count = s.count("bar")
print(count)

# Encode string as a byte sequence.
# Default encoding is UTF-8. Default error handling is strict.
byte_sequence = s.encode()

# Does the string end with given substring? Takes optional start/end args to limit search range.
has_suffix = s.endswith("baz")
print(has_suffix)

# Convert tabs to spaces. Named tabsize=8 default.
s2 = stabs.expandtabs(tabsize=4)
print(s2)

# Return first index of string to search for.
# Optional start/end args to limit range.
# Returns -1 if not found.
index = s.find("bar")
print(index)






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

# Note that you can use multiline strings for multiline commenting.
"""
# Some lines we want to "comment" out.
a = 2
b = 3
c = 4
s = 'comment this stuff out' # Let's go!
print(s)
"""

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

# Use a string as a formatter.
# Using just {} as placeholders replaces them in order.
# You can use {0}, {1}, {2}, etc. to switch up the order.
# You can pass named args and interpolate them via {name}
s = "{} {}".format(1, 2)
print(s)
s = "{1} {0}".format(1, 2)
print(s)
s = "{1} {0} {foo}".format(1, 2, foo="value")
print(s)

# Pass in stuff to interpolate into format string via dictionary (map).
d = {"k1": 3, "k2": 4}
s = "{k1} {k2}".format_map(d)
print(s)
s = "{k1} {k2}".format(**d) # Same thing, essentially.
print(s)

# Return first index of string to search for.
# Optional start/end args to limit range.
# ValueError if not found.
s = "foo bar baz"
index = s.index("bar")
print(index)

# Boolean validation checks on string contents.
s.isalnum() # alphanumeric
s.isalpha() # alphabetic
s.isascii() # ASCII, no Unicode
s.isdecimal() # all decimal digits, 0-9
s.isdigit() # only digits, including Unicode characters like numeric superscripts
s.isidentifier() # valid Python identifier (does not exclude keywords)
s.islower() # lowercase characters
s.isnumeric() # even broader than isdigit(): includes fraction chars, Roman numerals, etc.
s.isprintable() # all characters in string are printable
s.isspace() # all whitespace: spaces, tabs, newlines, etc.
s.istitle() # simple title case string (not grammatical)
s.isupper() # uppercase

# Use string as separator to join a list of other strings.
# You have to pass it a list of strings. It does not autoconvert.
s = "...".join(map(str, [3, 2, 1, 0]))
print(s)

# Left justify a string within a given width field using a given padding character (defaults to space).
s = "foo bar baz"
s2 = s.ljust(20, '_')
print(s2)

# Convert to lowercase.
s = "FOO BAR BAZ"
s = s.lower()
print(s)

# Strip whitespace (by defaultu) from left of string.
# Pass it a chars string to strip those characters instead.
s = "    foo bar baz"
s = s.lstrip()
print(s)

# Partition string into a 3-tuple of strings using given separator string.
t = s.partition("bar")
print(t)

# Remove prefix.
s2 = s.removeprefix("foo")
print(s2)

# Remove suffix.
s2 = s.removesuffix("baz")
print(s2)

# Replace occurrences of old substring with new substring.
# Use count arg to limit number of replacements performed.
s2 = s.replace(" b", "XX", 1)
print(s2)

# Return first index of string to search for, starting from end of string.
# Optional start/end args to limit range.
# Returns -1 if not found.
index = s.rfind("bar")
print(index)

# Return first index of string to search for, starting from end of string.
# Optional start/end args to limit range.
# ValueError if not found.
index = s.index("bar")
print(index)

# Right justify a string within a given width field using a given padding character (defaults to space).
s = "foo bar baz"
s2 = s.rjust(20, '_')
print(s2)

# Partition string into a 3-tuple of strings using given separator string.
# Looks for separator starting from the end of the string.
t = s.rpartition("bar")
print(t)

# Split string into list using separator string arg (sep). Starting from end of string.
# The split list is still in left-to-right order like the string, not reversed.
# sep defaults to None; this splits the string by whitespace.
# maxsplit -- maximum number of splits to do
L = s.rsplit()
print(L)

# Strips whitespace (by default) from a string.
# Pass it a chars string to strip those characters instead.
s = "foo bar baz \t\n"
s = s.rstrip()
print(s)

# Like rsplit() but starts at beginning of string.
L = s.split()
print(L)

# Split string into list of lines.
# Don't keep newlines as part of each line. Override this with keepends=True.
s2 = "foo\nbar\nbaz\n"
L = s2.splitlines()
print(L)

# See if a string starts with some prefix.
# You can also give it a tuple of prefixes to check.
# Optional start/end args to limit range.
has_prefix = s.startswith("fo")
print(has_prefix)

# Like doing lstrip() and rstrip(). Strips from both sides.
s = "  foo bar baz  "
s = s.strip()

# Invert case of all letters.
s2 = s.swapcase()
print(s2)

# Apply simple title case to string. Not grammatical.
s2 = s.title()
print(s2)

# Translate string using a map of Unicode ordinals to Unicode ordinals, strings, or Nones.
# Unicode ordinals would be the integer code point values, I think.
# Each occurrence in original string is replaced by mapped value.
#
# Create translation dictionary that converts a -> o, e -> i, and deletes b.
# maketrans() is the only public static method of the string class (str).
translation = str.maketrans("ao", "ei", "b")
s2 = s.translate(translation)
print(s2)

# Left pad string with zeroes to given width.
s2 = "123"
s2 = s2.zfill(7)
print(s2)




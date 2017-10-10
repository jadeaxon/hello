#!/usr/bin/env python3

# Assign a string containing at least one escaped char.
tabby_cat = "\tI'm tabbed in."
# Assign a string containing at least one escaped char.
# Note that no escape is necessary for #.
persian_cat = "# I'm split\non a line."
# Assign a string containing at least one escaped char.
backslash_cat = "I'm \\ a \\ cat."

# Assign a triple-quote string which includes escaped chars.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Try same thing with '''.
# Note that ' does not suppress escapes as in Bash.
# It only makes it easier to use literal "s.
thin_cat = '''
I'll do a list:
\t* Cat food
\t* Swedish "fish"
\t* Catnip\n\t* Grass
'''

# Print.
print(tabby_cat)
# Print.
print(persian_cat)
# Print.
print(backslash_cat)
# Print.
print(fat_cat)
# Do drill #2.
print(thin_cat)



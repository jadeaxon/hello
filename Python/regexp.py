#!/usr/bin/env python

# Python's regular expressions module.
import re

# Find all words that befin with lowercase f and shove them in a list.
# Notice the use of Python's raw quotes.
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

# Remove duplicated words and replace them with a single instance of the word.  Destutter.
print re.sub(r'(\b[a-z]+) \1', r'\1', 'The cat in in in the the hat hat.')



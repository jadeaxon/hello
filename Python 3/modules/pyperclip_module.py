#!/usr/bin/env python3

import warnings
import pyperclip

# On Cygwin it warns about pyperclip not working perfectly in Cygwin.
with warnings.catch_warnings(action="ignore"):
    pyperclip.copy("stuff to put on clipboard") # Copy to clipboard.
    s = pyperclip.paste() # Get text from clipboard. Paste it to string s.

print("Got from clipboard:", s)



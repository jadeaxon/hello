#!/usr/bin/env python3

import random

flashcards = {
    r'\n': 'ASCII linefeed (LF=10); aka, newline',
    r'\t': 'ASCII horizontal tab (TAB=9)',
    r'\a': 'ASCII bell (BEL=7)',
    r'\#': 'DNE: # does not need to be escaped',
    r'\\': 'backslash',
    r'\'': 'single quote (when inside double quotes)',
    r'\"': 'double quote (when inside single quotes)',
    r'\f': 'ASCII formfeed (FF=12)',
    r'\b': 'ASCII backspace (BS=8)',
    r'\N{name}': 'Unicode character by name',
    r'\r': 'ASCII carriage return (CR=13)',
    r'\v': 'ASCII vertical tab (VT=11)',
    r'\uxxxx': 'Unicode char with 16-bit hex value xxxx',
    r'\Uxxxxxxxx': 'Unicode char with 32-bit hex value xxxxxxxx',
    r'\ooo': 'Character with octal value ooo; can use 1-3 octal digits',
    r'\0': 'Octal 0, the ASCII NUL character; not a string terminator in Python',
    r'\xhh': 'Character (or byte when in bytes literal) with hex value hh'
}

keys = list(flashcards.keys())
while True:
    try:
        key = random.choice(keys)
        print(key, end="")
        input()
        value = flashcards[key]
        print(value)
        print()
    except KeyboardInterrupt:
        break



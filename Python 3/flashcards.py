#!/usr/bin/env python3

import random

flashcards = {
    r'\n': 'ASCII linefeed (LF); aka, newline',
    r'\t': 'ASCII horizontal tab (TAB=9)',
    r'\a': 'ASCII bell (BEL)',
    r'\#': 'DNE: # does not need to be escaped',
    r'\\': 'backslash',
    r'\'': 'single quote',
    r'\"': 'double quote',
    r'\f': 'ASCII formfeed (FF=12)',
    r'\b': 'ASCII backspace (BS)',
    r'\N{name}': 'Unicode character by name',
    r'\r': 'ASCII carriage return (CR)',
    r'\v': 'ASCII vertical tab (VT)',
    r'\uxxxx': 'Unicode char with 16-bit hex value xxxx',
    r'\Uxxxxxxxx': 'Unicode char with 32-bit hex value xxxxxxxx',
    r'\ooo': 'Character with octal value ooo',
    r'\xhh': 'Character with hex value hh'
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



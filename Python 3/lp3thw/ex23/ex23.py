#!/usr/bin/env python3

# PRE: Your shell is configured to use UTF-8.
# PRE: languages.txt is UTF-8.

# <script> utf-8 strict

# Import the sys module so we can use sys.argv for command-line args.
import sys
script, encoding, error = sys.argv

# Prints a line showing encoded vs. raw bytes for each line of 
# language file.  Stops at first blank line.
# main() is the typical entry point for other languages like C++.
def main(language_file, enconding, errors):
    # Read next line of language file.
    line = language_file.readline()

    # If line is not blank, process it and then do the next line.
    if line:
        print_line(line, encoding, errors)
        # Recursion.
        return main(language_file, encoding, errors)
    # If a line is blank, stop processing the file.

# Processes a single line of the file.
# raw_bytes -- a sequence of bytes
# Python displays these as a b'' byte literal string.
# Decoding the bytes (according to the encoding) creates a string.
# A codec (encoder/decoder) can translate both ways.
# How exactly does Python store its strings internally?
def print_line(line, encoding, errors):
    next_lang = line.strip() # Remove the trailing newline.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)

# Open the languages file and run the main program on it.0
languages = open("languages.txt", encoding="utf-8")
# languages = open("binary.docx", encoding="utf-8")

main(languages, encoding, error)

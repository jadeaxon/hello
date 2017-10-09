#!/usr/bin/env python3

# A formatter is a string containing placeholders like {} to be replaced by values.
formatter = "{} {} {} {}"

# Replace the placeholders with numbers.
print(formatter.format(1, 2, 3, 4))
# Replace the placeholders with numbers as words.
print(formatter.format("one", "two", "three", "four"))
# Replace the placeholders with boolean values.
print(formatter.format(True, False, False, True))
# Replace the placeholders with other formatters.
# You could build up a more complicated formatter this way.
print(formatter.format(formatter, formatter, formatter, formatter))
# Break a function call up across multiple lines.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))



#!/usr/bin/python3

# Unlike in Python 2, you need to use () with print.
print("Put", "space", "between", "args.")
print("Automatically append a newline.")
print()
print("Suppress newline with the named arg 'end'", end="")
print(" as above.")

# Default separator is a space. Override using sep arg.
# Default line end is newline. Override with end arg.
print("foo", "bar", "baz", sep="-", end="|")
print()

# Use escape sequences via escape character, \.
# print("\") # Syntax error.
print("\\") # Print \.
print("\n") # newline
print("Double quote: \"")
print('Single quote: \'')
print("Single quotes '' inside double quotes.")
print('Double quotes "" inside single quotes.')
print("line \
continuation")

# Use formatted strings to use variable values inside them.
name = "Jeff"
age = 40
# printf style format string with % operator to bind a tuple to formatter.
print("%s is %d." % (name, age))
# A Pythonic format string.
print("{0} is {1}.".format(name, age))
# An actual formatted string (and f-string).
print(f"{name} is {age}.")

print(
"""
Print
a
multiline
string.
""", end=""
)

message = "print me!"
print(
f"""
Multiline formatted string:
{message}
""", end=""
)

# You can print to a file. You can use this to print to stderr.
# You'll probably want to use the logging module instead of printing to stderr though.
# Or use open() to get some other file to print to.
import sys
print('ERROR: Printing to stderr.', file=sys.stderr)

# Print acts like a procedure. In Python, there are no procedures, so it just returns None.
# None is the equivalent of null in other languages.
result = print("Print doesn't return anything useful. Acts like a procedure.")
print(result)
print(type(result))




#!/usr/bin/env python3

# Prints a string literal.
print("Mary had a little lamb.")
# Uses format() method to replace {} placeholder.
print("Its fleece was white as {} {}.".format('yellow', 'snow'))
# Prints a string literal.
print("And everywhere that Mary went.")
# Use * overload to print a string multiple times.
print("." * 12) # What'd that do?

# A one-character string.
end1 = "L"
# A one-character string.
end2 = "e"
# A one-character string.
end3 = "m"
# A one-character string.
end4 = "o"
# A one-character string.
end5 = "n"
# A one-character string.
end6 = "a"
# A one-character string.
end7 = "d"
# A one-character string.
end8 = "e"
# A one-character string.
end9 = "r"
# A one-character string.
end10 = "a"
# A one-character string.
end11 = "d"
# A one-character string.
end12 = "e"

# Watch that comma at the end.  Try removing it to see what happens.
# Append strings with + operator.  Use 'end' named arg to suppress default newline.
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
# Append strings.
print(end7 + end8 + end9 + end10 + end11 + end12)


#!/usr/bin/env python3

# Prints a string literal.
print("Mary had a little lamb.")
# Uses format() method to replace {} placeholder.
print("Its fleece was white as {}.".format('snow'))
# Prints a string literal.
print("And everywhere that Mary went.")
# Use * overload to print a string multiple times.
print("." * 10) # What'd that do?

# A one-character string.
end1 = "C"
# A one-character string.
end2 = "h"
# A one-character string.
end3 = "e"
# A one-character string.
end4 = "e"
# A one-character string.
end5 = "s"
# A one-character string.
end6 = "e"
# A one-character string.
end7 = "B"
# A one-character string.
end8 = "u"
# A one-character string.
end9 = "r"
# A one-character string.
end10 = "g"
# A one-character string.
end11 = "e"
# A one-character string.
end12 = "r"

# Watch that comma at the end.  Try removing it to see what happens.
# Append strings with + operator.  Use 'end' named arg to suppress default newline.
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
# Append strings.
print(end7 + end8 + end9 + end10 + end11 + end12)


#!/usr/bin/env python3

# Integer literals.
i = 123
i = +123
i = -123
i = 1_000_000
i = int("123")

# You don't have to use _s where they really should go.
i = 1_2_3_4 # 1234

# Hexidecimal.
i = 0xFACE
i = 0xface
i = 0Xface

# Octal.
i = 0o777
i = 0O777

# Binary.
i = 0b1101
i = 0B1101

# You can use _ in any kind of integer literal.
i = 0xFACE_FACE
i = 0o777_666
i = 0b1101_0011

# Printing hex/oct/bin literals outputs the decimal version.
print(0b1101)

# Floating point literals.
f = 4.0
f = -4.0
f = 4.
f = 0.4
f = .4
f = float("3.14")
f = 3e8 # Scientific notation, <base>e<exponent>: 3 * 10^8
f = 3E8
f = -3.14e7
f = -3.14e-2

# You can use _s in float literals too. And use them badly.
f = 1_234.45
f = 1_2_3.4_5

# When you print floats, Python displays the most concise representation (excluding the lone .
# form).

# String literals.
s = "" # Empty string (evaluates as false).
s = "string"
s = 'string'
s = "Quoting \" double quotes"
s = f"f-string {3 + 2}" # Can interpolate expressions using {<expression>}.
s = """
multiline
string
"""
s = f"""
multiline
f-string
{3 + 2}
"""

# NoneType (null) literal.
n = None
if n is None:
    print("The void.")

# Boolean literals.
b = True
b = False

# List literals.
l = [] # Empty list. Evaluates as false.
l = [1, 2, 3]
l = ["one", 2, 3] # mixed types in list
l = [[1, 2], [3, 4]] # nested list
l = list("string") # convert to list of single characters

# Tuple literals.
t = ()
t = (1, 2, 3)
t = 1, 2, 3 # You can omit the parenthesis.
t = tuple([1, 2, 3]) # conver list to tuple

# Dictionary literals.
d = {}
d = {"key1": "value1", "key2": "value2"}




#!/usr/bin/env python3

# Unary plus. Rarely used.
+1

# Unary minus.
-1

# Binary plus. Addition.
# Operators actually call various dunder methods like __add__ under the hood.
# This lets you override operators in your own classes.
i = 1 + 1
i = int(1).__add__(1) # Same thing.
# NO: 1.__add__(1) # Can't call a method directly on an int literal.
print(i)

# For strings, it is concatenation.
s = "first string" + "second string"
print(s)

# Binary minus. Subtraction.
i = 1 - 1
print(i)

# For + and -, if either operand is a float, the result is a float.
f = 1 + 2.0
f = 2.0 - 1
print(f)

# You can't subtract strings.
try:
    s = "first string" - "second string"
except Exception as e:
    print(e)

# Numeric multiplication.
i = 3 * 2
print(i)

f = 3.3 * 2.0
print(f)

f = 3.2 * 2 # Mixing int and float results in float.
print(f, type(f))

# String replication.
s = "repeat me" * 3
print(s)

# Exponentiation.
i = 2 ** 3 # 2 to the power of 3
f = 2.1 ** 3
f = 3.2 ** .5 # Same as square root.
print(f)

# Division.
f = 3 / 2
f = 3.1 / 2
f = 3.2 / 2.1
print(f)
print()

# Division by zero does not work.
try:
    f = 3 / 0
except Exception as e:
    print(e, type(e))

# Integer division. Floor division.
print("Integer (floor) division:")
i = 3 // 2 # 1
print(i)
i = 1 // 2 # 0
print(i)
i = -1 // 2 # -1 (rounds to next int below normal division result)
print(i)
print()

# Modulo. Remainder.
print("Modulo (remainder):")
i = 3 % 3 # 0
print(i)
i = 6 % 3 # 0
print(i)
i = 5 % 3 # 2
print(i)

# You can do % with floats too.
# x % y == x - ((x // y) * y)
f = 3.2 % 3
print(f)


# Operator precedence.
# Multiplication happens before addition.
# *, /, //, and % bind before binary + and -.
i1 = 3 * 2 + 2
i2 = (3 * 2) + 2 # Use parenthesis to force evaluation order.
print(i1 == i2)

# Most operators bind left.
i1 = 7 % 5 % 2
i2 = (7 % 5) % 2
print(i1 == i2)

# Exponentiation binds right.
i1 = 2 ** 3 ** 4
i2 = 2 ** (3 ** 4)
i3 = (2 ** 3) ** 4
print(i1 == i2) # True
print(i1 == i3) # False

# Exponentiation binds before unary minus (surprisingly).
# But only for the left operand.
i1 = -3 ** 2
i2 = (-3) ** 2
i3 = -(3 ** 2)
print(i1 == i2) # False (!).
print(i1 == i3) # True

# x ** -n == 1/(x ** n)
i1 = 2 ** -1
i2 = 1/(2 ** 1)
print(i1 == i2)

# Augmented operators, aka shortcut assignment operators, aka in-place assignment operators.
# There are no ++ and -- operators in Python.
i = 0
i += 1 # i = i + 1
i -= 1 # i = i - 1
i *= 2
i /= 2 # i is now a float
i = int(i)
i %= 1
print(i)

i = 2
i **= 2 # 4

# Comparison operators.
# They evaluate to a boolean value.
# Mixed comparisons between int and float work.
True is True # identity; the two objects are the exact same object
True is not False
True == 1 # equality; the two objects are considered to be equivalent in value
3 == 3.0
1 != 2 # inequality
2 > 1 # greater than
2 >= 1 # greater than or equal to
1 < 2 # less that
1 <= 2 # less than or equal to

"apple" < "banana" # you can compare strings

# Bitwise operators. Bit twiddling.
# Treat ints like a bit sequence. Results in an int.
i = 0b1111 & 0b0100 # Bitwise and.
print(bin(i)) # 0b100 (won't show leading zeroes)
print(f"{i:08b}") # Width 8, left pad with 0, get rid of the 0b prefix.

i = 0b1010 | 0b0101 # Bitwise or.
print(f"{i:08b}") # 00001111

i = 0b1001 ^ 0b0001 # Bitwise xor.
print(f"{i:08b}") # 00001000

i = ~0b1001 # Bitwise negation.
print(f"{i:08b}") # You might expect 11110110, but you get -0001010.
# Python is evaluating the bits as negative number.
# But then showing you the bits for a positive number and adding a negative sign.
# There is a way to get the actual bits.
i &= 0xFF # Turns the number back into a positive number but with the final 8 bits preserved.
print(f"{i:08b}") # Now we get the expected 11110110.
# Also note from the above that all the bitwise operators have assignment shortcut operators too.

# To set individual bit in any number.
bitmask_3 = 0b100 # 3rd bit
i = 0b1000
i |= bitmask_3 # Set the 3rd bit. Leave everything else as is.
print(f"{i:08b}") # 00001100

i &= ~bitmask_3 # Clear the 3rd bit. And with negated bitmask.
print(f"{i:08b}") # 00001000

# Use the left shift operator to make a bitmask for the 8th bit.
bitmask_8 = 1 << 7 # 8th bit
i |= bitmask_8 # Set 8th bit
print(f"{i:08b}") # 10001000

bitmask_7 = 1 << 6 # 7th bit
i ^= bitmask_7 # Toggle/flip the 7th bit.
print(f"{i:08b}") # 11001000
i ^= bitmask_7 # Toggle/flip the 7th bit.
print(f"{i:08b}") # 10001000

# There is also bitwise shift right. It is equivalent to floor dividing by 2.
# Left shifting by 1 bit multiplies by 2.
i = 77
print(i // 2, i >> 1)

# The in and not in operators.
'a' in {'a', 'b', 'c'} # set
'substring' in 'string with substring' # string
1 in [1, 2, 3] # list
"key" in {"key": "value"} # dictionary

fruit = {'banana', 'apple', 'pear'}
"truck" not in fruit







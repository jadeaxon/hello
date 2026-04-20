#!/usr/bin/env python3

# f-string, formatted string literal
# Interpolates {<expression>} placeholders.
name = 'f-string'
s = f"Hello, {name}!"
print(s)

# Use {{ and }} for literal { and }.
s = f"{{ and }}"
print(s)

# Use an arbitrary expression. Though maybe you shouldn't.
s = f"{min((5 * 6) + 2, -1)}"
print(s)

# The placeholder can have format specifier.
# {<expression>:<format specifier>}
s = f"{3:.2f}" # display as float with 2 decimal places
print(s)

# The format specifier itself can use nested placeholders.
# The nested placeholds can even use their own format specifiers (not shown).
p = 3
s = f"{3:.{p}f}" # crazy!
print(s)

# The f-string is only interpolated once when encountered at runtime.
# Use str.format() or something else if you need to reuse a formatting template.




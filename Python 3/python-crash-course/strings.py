s = "string literal"
s = 'string literal'

# Method to convert to title case.
s = "jeff anderson"
s = s.title()
print(s)

s = s.lower()
print(s)
s = s.upper()
print(s)

# Format strings (f-strings). Put an f before the quote. Put expressions inside {}.
print(f"My name is {s.title()}.")

# Split a multiline string.
multiline = "This string\nhas multiple\nlines."
lines = multiline.splitlines()
print(lines)

template = 'Replace <token> <token> with something else.'
count = template.count('<token>') # Count occurrences of a string in another string.
content = template.replace('<token>', 'value') # Replace all occurrences. Does not change original string.
print(f'Replaced {count} occurrences.')
print(content)



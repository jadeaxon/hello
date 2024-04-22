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
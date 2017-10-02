#!/usr/bin/env python3

# Old joke.  10 is 2 in binary.
types_of_people = 10
# The joke.
x = f"There are {types_of_people} types of people."

# Superfluous variable #1.
binary = "binary"
# Superfluous variable #2.
do_not = "don't"
# More var expansions inside f-strings.
y = f"Those who know {binary} and those who {do_not}."

# Print first string.
print(x)
# Print secord string.
print(y)

# Use an f-string inside another f-string.
print(f"I said: {x}")
# No, single quotes inside the string do not block substitution.
print(f"I also said: '{y}'")

# Boolean literal False.  The joke is slightly funny but not hilarious.
hilarious = False
# Correct evaluation of the joke.
joke_evaluation = "Isn't that joke so funny?! {}"
# Using the format method of a string instead of an f-string.
print(joke_evaluation.format(hilarious))

# Left operand.
w = "This is the left side of..."
# Right operand.
e = "a string with a right side."

# The plus operator is overloaded for string concatenation.
print(w + e)


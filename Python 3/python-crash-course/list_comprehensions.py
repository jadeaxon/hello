# List comprehensions. Ways to concisely initialize lists dynamically.

# <list> = [<expression using var> for <var> in <list expression>]
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# List comprehension for the cubes of 1..10 inclusive.
cubes = [value ** 3 for value in range(1, 10 + 1)]
print(cubes)
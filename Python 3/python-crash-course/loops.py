weapons = ['knife', 'sword', 'mace', 'dagger']

# You should not modify elements in for loops. Use a while loop.
# You can use continue and break in loops. 
# Are there labels to break/continue outer loops?

# A simple for each (for in) loop over a list.
for weapon in weapons:
    # The loop block is determined by indentation.
    print(weapon)

print('Now outside the loop.')

# Loop over a range of numbers, [1, 5). Non-inclusive end. The range function returns a list, sort of (actually it is a generator).
# range(5) -> 0..4
for value in range(1, 5):
    print(value)

# To get a list from range(), use list().
numbers = list(range(6))
for value in numbers:
    print(value)

# Count by 2 instead of 1.
evens = list(range(2, 11, 2)) # [2, 4, 6, 8, 10]
print(evens)

# Print the square of each even number.
# Build up a list based on another list. A transformation of the list.
squares = []
for x in evens:
    square = x ** 2
    squares.append(square)
print(squares)

# Summary functions. Reduce a list to a single value.
print(min(squares))
print(max(squares))
print(sum(squares))
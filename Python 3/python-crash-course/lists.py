# Lists.

# Create a list of games.
games = [] # You can have an empty list. A list literal value.
games = ['Fallout 2', "Baldur's Gate 3", 'Rome: Total War', 'Ys Book IV: The Dawn of Ys']
print(games)

# The first game in list of games. 0-based index.
first_game = games[0] # This stores a copy of the value in the list.
message = f"The first game in the list is {games[0]}."
print(message)

# The last element. And 2nd to last element.
print(games[-1])
print(games[-2])

# Modify the list.
games[0] = 'Fallout 3'
print(games[0])
print(first_game) # Is a variable a pure reference? No.

# Append to the list.
games.append("GTA 6")
print(games)

# Insert before first element.
games.insert(0, "Super Mario: Wonder")
print(games)

# Delete an element. Not a list method for some reason.
del games[0]
print(games)

# Pop from end of list. Removes and returns last element. Treat it like a stack.
last_game = games.pop()
print(last_game)

# You can pop from any position.
first_game = games.pop(0)
print(first_game)
print(games)

# Remove a game by value.
games.append("trash")
games.remove("trash")

# Reverse order of list. Mutates.
games.reverse()
print(games)
print()

# Sort a list. Mutates. Alphabetical ascending by default.
fruit = ['pear', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'apple']
print(fruit)
fruit.sort()
print(fruit)

# Reverse sort.
# Note you have named method parameters. And True (case-sensitive) is a boolean literal.
fruit.sort(reverse=True)
print(fruit)
print()

# For a non-mutating sort, use sorted() global function.
print("Using sorted() global function:")
print(sorted(fruit))
print(fruit)

# Global function len() for list length.
list_length = len(fruit)
print(f"The length of the fruit list is {len(fruit)}.")

# Out of range index.
# IndexError: list index out of range
# dne = fruit[7]

# Make a copy of a list using slice notation.
fruit_copy = fruit[:]
fruit_copy.pop()
print(len(fruit))
print(len(fruit_copy))


#!/usr/bin/env python3

D = {} # Empty dictionary.
D = dict() # Same
print(D)

# Create a dictionary from a list of keys. Each item will have the same value.
value = 0
D = dict.fromkeys(["one", "two", "three"], value)
print(D)

# A dictionary with 3 key/value pairs (items).
D = {"one": 1, "two": 2, "three": 3}

v = D["one"] # Look up a value by key. KeyError if DNE.
v = D.get("one", "default value") # Alternate way that avoids KeyError.
print(v)

D["four"] = 4 # Add a new key/value pair.
print(D)

del D["four"] # Remove an item.
print(D)

# Iterate over dictionary items.
for key, value in D.items():
    print(f"{key} = {value}")

for key in D.keys():
    print(f"{key} = {D[key]}")

for key in D:
    print(f"{key} = {D[key]}")

# Iterate over just the values.
for value in D.values():
    print(value)

# There are no dictionary slices. Slices require integer-only indexes.

# Make a copy.
D2 = D.copy()

# Remove all items.
D.clear()
print(D)
D = D2.copy()

# Add items from another dictionary. Overwrites existing items with same keys.
# D.extend({"seven": 7, "eight": 8}) # NO: No extend method.
D.update({"seven": 7, "eight": 8})
D.update({"seven": 77, "eight": 88})
print(D)

# Remove a specific item and return its value.
v = D.pop("one")
D["one"] = v

# Items are popped by reverse order of insertion (LIFO).
D.clear()
D["one"] = 1
D["two"] = 2
D["three"] = 3
while D:
    item = D.popitem()
    print(item)
D = D2.copy()

# Set a key's value only if it does not already exist.
D.setdefault("four", 4)
D.setdefault("four", 5) # Does nothing.
print(D["four"])




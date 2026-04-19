#!/usr/bin/env python3

D = {} # Empty dictionary.
bool(D) # Empty dictionary is False.
D = dict() # Same
print(D)

# Create a dictionary from a list of keys. Each item will have the same value.
value = 0
D = dict.fromkeys(["one", "two", "three"], value)
print(D)

# Create a dictionary from a list of tuples.
# Zip two equal size lists to form a dictionary.
# zip gives you a sequence of tuples with elements at same index for given sequence args.
L1 = ["one", "two", "three"]
L2 = [1, 2, 3]

# You can use dict() to turn any sequence of 2-tuples (pairs) into a dictionary.
# If same key is used more than once, the latest value is kept.
D = dict(zip(L1, L2))
print("From zipped lists:")
print(D)

# Create dictionary via dictionary comprehension.
D = {k: 0 for k in L1}
print("From comprehension:")
print(D)

# A dictionary with 3 key/value pairs (items).
D = {"one": 1, "two": 2, "three": 3}

length = len(D) # Number of items.
print(length)

v = D["one"] # Look up a value by key. KeyError if DNE.
v = D.get("one") # Returns None if DNE.
v = D.get("one", "default value") # Returns given default value if DNE.
print(v)

# Check if key is in dictionary or not
b = "one" in D
print(b)
b = "one" not in D
print(b)

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






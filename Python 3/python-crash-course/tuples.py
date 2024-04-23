# Tuples.
# They are basically immutable lists.
# You'd use them for a multi-part value like a 3D coordinate: (x, y, z).

coordinate = (2, 3, 4)
print(coordinate[0]) # First value in tuple.
print(coordinate)

# No--immutable.
# coordinate[0] = 5

# Not sure why you'd want this.
one_element_tuple = (17,)

# You can loop over a tuple just like a list.
for part in coordinate:
    print(part)
# List slices.

sodas = ['Coke', 'Sprite', 'Mountain Dew', 'Fanta Orange', 'A&W Root Beer', 'Pepsi']

sodas_slice = sodas[0:2] # List slice of elements 0 and 1.
print(sodas_slice)

sodas_slice = sodas[2:] # 3rd (index 2) element to the end.
print(sodas_slice)

sodas_slice = sodas[0:-1:2] # Every other element.
print(sodas_slice)

# Use a slice to copy a list.
sodas_copy = sodas[:]
print(sodas_copy)

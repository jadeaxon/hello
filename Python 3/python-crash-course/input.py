# User input.

# Get a string from user.
response = input('Enter a value: ')
print(response)

# Get an integer.
response = input('Enter an integer: ')
number = int(response) # Raises a ValueError if can't convert to integer.
if number > 3:
    print("The number you entered was greater than 3.")

# Keep asking user for a string until they type 'exit'.
iteration = 0
while True:
    iteration += 1
    string = input(f"Enter a string (type 'exit' to quit) [{iteration}]: ")
    if string == 'exit': break
    print(string.lower())

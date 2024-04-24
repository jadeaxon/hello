# Exceptions. Runtime errors.

# They are objects.

# You can catch exceptions using try-except blocks.
try:
    x = 5 / 0 # Try to divide by zero.
    # Causes a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    # Runs if the try block does not raise an exception.
    print('Operation successful. No exceptions raised.')

# FileNotFoundError
from pathlib import Path
file = Path('DNE.txt')
try:
    contents = file.read_text()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print(contents)

# Silently swallow an exception. Use the special pass keyword.
print('Silently ignore exception.')
try:
    x = 5 / 0
except ZeroDivisionError:
    pass
print('Program continues to run.')


# ValueError
input = input('Enter an integer: ')
try:
    i = int(input) # Convert string to integer.
except ValueError:
    print(f'{input} is not an integer.')
else:
    print(f'You entered integer {i}.')







    
# If statements. Branching.

# if <boolean expression>:
#     <true block>
# else:
#     <false block>

condition = True # Assign boolean literal to a variable.
if condition:
    print('The condition is true.')
else:
    print('The condition is false.')


# Use an if statement inside a for loop.
cars = ['Toyota', 'Ford', 'Mazda', 'Tesla', 'Kia']
for car in cars:
    if car == 'Tesla':
        print(car)
    else:
        print('This car is not a Tesla.')

# Boolean operators.
# ==
# !=
# <, <=, >, >=
# and, or, not
# <element> in <list>

# Check if a value is in a list.
if 'Toyota' in cars:
    print('Toyota is in the list of cars.')

if 'Ferrari' not in cars:
    print('Ferrari is not in the list of cars.')


age = 23
if age < 18:
    print('You are a mere child.')
elif age < 30:
    print('You are quite young.')
elif age < 50:
    # You can have multiple elif blocks.
    print('You are not old yet')
else:
    # The else block is not required.
    print('You are getting up there.')


# Check if a list is not empty.
things = ['foo', 'bar', 'baz']
if things:
    print(f'The list is not empty: {things}.')









# Dictionaries.
# Hash maps. Collections of key/value pairs. Associative arrays.
# Like how a normal dictionary has a word (key) and its definition (value).
# An array that uses non-numeric indexes.

# The key can be a number, string, list, or even a dictionary.
# The value can also be anything.

# Let's suppose you have an alien invaders video game.
# As part of that game world, there is a group of aliens. Let's put them in a list.

aliens = []

# Each alien has a color and a number of points you earn by destroying it.
# These attributes can be stored in a dictionary that maps attribute names to values.

# We create the first alien.

# Does a non-existent list element autovivify? Nope!
# aliens[0] = {'color': 'green', 'points': 5}

# {} is used for dictionary literals.
aliens.append({})
aliens[-1] = {'color': 'green', 'points': 5}

# Let's add another alien.
aliens.append({})
aliens[-1] = {'color': 'red', 'points': 10}

print(aliens)

for alien in aliens:
    color = alien['color'] # Get a value from a hash.
    print(color)

# Let's give the alien an (x,y) location tuple.
aliens[0]['location'] = (5, 5)
aliens[1]['location'] = (10, 5)

for alien in aliens:
    location = alien['location']
    print(location)

# Whatever this game world state is, you can render it as graphics or text (like in old games like Zork).
# The players perception of the game world may not reflect its real or total state.
# For example, imagine if the player goes temporarily blind. Or drinks a potion that makes them hallucinate.

# Use del to remove a key/value pair.
alien = aliens[0]
del alien['location']
print(alien)

# Use get() to access a dictionary value. You can provide a default value.
# We've get a KeyError error if we tried to use alien['location'] here since we just deleted it.
# Also, get() returns None instead of raising an error if no value exists (really no key exists).
# The None literal is like null in other languages.
location = alien.get('location', (0, 0))
print(location)
location = alien.get('location')
print(location)

# While dictionaries often store all the attributes for a single object, they can also store the same
# attribute for multiple objects. This is more of a mapping.
# For example, you might store the state each city is part of. Map cities to states.
city_to_state = {}
city_to_state['Los Angeles'] = 'California'
city_to_state['San Diego'] = 'California'
city_to_state['Salt Lake City'] = 'Utah'

# You might store the count for each letter or word in a document. Things like that.

# Loop through the key/value pairs in a dictionary.
# Note you need to call .items().
# Dictionary items are stored in the order that they were added. 
print()
print('Looping through a dictionary.')
for key, value in alien.items():
    print(f"{key} => {value}")

# You can also loop through just the keys.
for key in alien.keys():
    print(key)

print()
print('Looping through a dictionary, sorted.')
alien['location'] = (1, 1)
# Loop through dictionary items in sorted order.
for key in sorted(alien.keys()):
    print(f'{key} => {alien[key]}')


# You can just loop through the values if you want.
for state in city_to_state.values():
    print(state)

# If you want just the unique values, put them in a set.
print("Uniqued list of values via a set:")
for state in set(city_to_state.values()):
    print(state)

# {} is used to create set literals.
set_of_states = {'CA', 'GA', 'UT', 'CA'}
print(set_of_states) # Note that the duplicates get removed.














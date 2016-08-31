#!/usr/bin/env python

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['UT'] = 'Provo'
cities['PA'] = 'Pittsburgh'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

# We're putting a function in a hash?
cities['_find'] = find_city

while True:
    # The trailing comma causes print not to emit a newline.
    print "State? (Press ENTER to exit)",
    prompt = "> "
    state = raw_input(prompt)

    if not state: break

    # Call the function in the hash.
    city_found = cities['_find'](cities, state)
    print city_found



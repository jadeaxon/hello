#!/usr/bin/env python3

# Create a mapping of state to abbreviation.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Utah': 'UT',
}

# Create a basic set of states and some cities in them.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'UT': 'SLC'
}

# Add some more cities.
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities.
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])
print("UT State has:", cities['UT'])

# Print some states.
print('-' * 10)
print("Michigan's abbreviation", states['Michigan'])
print("Florida's abbreviation", states['Florida'])
print("Utah's abbreviation", states['Utah'])

# Do it by using the state then cities dict.
print('-' * 10)
print("Michigan has", cities[states['Michigan']])
print("Florida has", cities[states['Florida']])
print("Utah has", cities[states['Utah']])

# Print out every state abbreviation.
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")

# Print every city in state.
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}.")

# Now do both at the same time.
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}.")
    print(f"It has city {cities[abbrev]}.")

print('-' * 10)
# Safely get an abbreviation by state that might not be there.
state = states.get('Texas')
if not state:
    print("Sorry, Texas DNE.")

# Get a city with a default value.
city = cities.get('TX', 'DNE')

print(f"The city for the state 'TX' is {city}.")


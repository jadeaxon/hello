#!/usr/bin/env python3

import json

# JSON content looks very much like Python dict and list literal syntax.
json_string = '{ "name":"John", "age":30, "city":"New York"}'

# Parse the JSON into a Python object.
o = json.loads(json_string)

print(o["age"])

# The JSON might just be a list.
json_string = '["foo", "bar"]'
o = json.loads(json_string)
print(o[1])

# Convert a dict to JSON.
D = {
    "one": 1,
    "two": 2,
    "more": [3, 4, 5]
}
json_string = json.dumps(D)
print(json_string)

D2 = json.loads(json_string) # Reload from JSON.
print(D == D2) # Yup, they are the same.

# Make the JSON a bit more readable. Esp. if a long string.
json_string = json.dumps(D, indent=4)
print(json_string)



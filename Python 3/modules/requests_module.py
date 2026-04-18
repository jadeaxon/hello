#!/usr/bin/env python3

import requests

# Make an HTTP request and get a response.
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(response))
print(response.status_code) # HTTP 200 status if all went well.
response.raise_for_status() # Raise an exception if HTTP request failed.

# Use content from the response.
print(len(response.text)) # Content received from URL as a string is in response.txt.
line = response.text.split('\n')[0]
print(line)
print()

response = requests.get('https://automatetheboringstuff.com/files/DNE.txt')
response.raise_for_status() # Should get an HTTP 404 error.


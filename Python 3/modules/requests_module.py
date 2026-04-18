#!/usr/bin/env python3

import requests
import json

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

try:
    response = requests.get('https://automatetheboringstuff.com/files/DNE.txt')
    response.raise_for_status() # Should get an HTTP 404 error.
except Exception as e:
    print(e)

# Use an online weather API.
# FAIL: Getting 401 unauthorized error even though API key is activated.
# Looks like you have to additionally subscribe to a free-ish plan to make actual calls.
api_key = open('api_key.txt').read().strip()
print(api_key)

city = 'San Francisco'
state = 'CA'
country = 'US'
limit = 1
base_url = 'http://api.openweathermap.org/geo/1.0/direct'
query = f'?q={city},{state},{country}&limit={limit}&appid={api_key}'
url = base_url + query
print(url)
response = requests.get(url)
response.raise_for_status()

# The response content is JSON. Convert it to a Python dictionary.
data = json.loads(response.text)
print(data)



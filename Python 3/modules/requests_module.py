#!/usr/bin/env python3

import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(response))
print(response.status_code) # HTTP 200 status if all went well.
print(len(response.text)) # Content received from URL as a string is in response.txt.
line = response.text.split('\n')[0]
print(line)



#!/usr/bin/env python3

import requests
import bs4

# Get the page content.
res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()

# Parse the page into a document object model.
dom = bs4.BeautifulSoup(res.text, 'html.parser')

# Use a CSS selector to get all matching elements from model.
elements = dom.select('p')

# Get the content and attributes of each element.
for e in elements:
    print(e.get_text())
    print(e.attrs)





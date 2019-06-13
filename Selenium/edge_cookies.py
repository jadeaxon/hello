#!/usr/bin/python3

# PRE: pip install selenium
# In your virtualenv.
from selenium import webdriver

import time

# The above is just the WebDriver API.
# PRE: You also need the specific driver for Firefox.  It's the Gecko driver.
# Make sure you use the 64-bit driver for 64-bit Firefox.
# PRE: You need to add the location of that driver to your PATH.
# If using virtualenv, set this up in <env>/bin/activate.bat.

# Create a new Edge session.
edge = webdriver.Edge()
edge.implicitly_wait(30)
edge.maximize_window()

# Go to PROD AppNav.
# edge.get("https://userve.uvu.edu/applicationNavigator/seamless")

edge.get("https://www.duosecurity.com/barf")

cookies = edge.get_cookies()
for cookie in cookies:
    print(cookie)

# Quit Firefox.
edge.quit()


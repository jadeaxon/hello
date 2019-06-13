#!/usr/bin/python3

# Selenium does not support controlling a browser not created via the driver.
# A remote browser is one running on a remote system.
# You have to have Selenium Server running there to use it.

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

url = edge.command_executor._url
session_id = edge.session_id

edge = webdriver.Remote(command_executor=url, desired_capabilities={})
edge.session_id = session_id


edge.implicitly_wait(30)
# edge.maximize_window()

# Go to PROD AppNav.
# edge.get("https://userve.uvu.edu/applicationNavigator/seamless")

edge.get("https://www.timeanddate.com")

while True:
    edge.get(edge.getCurrentUrl()) # Refresh
    time.sleep(5)

# Quit Firefox.
edge.quit()


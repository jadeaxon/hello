#!/usr/bin/python3

# Selenium does not support controlling a browser not created via the driver.
# A remote browser is one running on a remote system.
# You have to have Selenium Server running there to use it.

# PRE: pip install selenium
# In your virtualenv.
from selenium import webdriver

import os
import time

# The above is just the WebDriver API.
# PRE: You also need the specific driver for Firefox.  It's the Gecko driver.
# Make sure you use the 64-bit driver for 64-bit Firefox.
# PRE: You need to add the location of that driver to your PATH.
# If using virtualenv, set this up in <env>/bin/activate.bat.

appdata = os.environ['APPDATA']

# Use about:profiles in Firefox.
# Selenium makes a copy of your profile.
# This should get you all your existing cookies, plugins/extensions, bookmarks, etc.
# NOTE: It takes about 10 seconds for Firefox to start.  Might be just from copying the profile.
profile = webdriver.FirefoxProfile(f'{appdata}\\Mozilla\\Firefox\\Profiles\\gll64sku.default-1517250148976')
firefox = webdriver.Firefox(profile)
firefox.maximize_window()
firefox.get("https://my.uvu.edu")

time.sleep(60)

firefox.quit()


#!/usr/bin/env python3

# PRE:
# pip3 install selenium
# pip3 install webdriver-manager

import sys
from selenium import webdriver
import webdriver_manager

if sys.platform == 'cygwin':
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager

    # This automatically finds/downloads the correct driver and sets the path
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
else:
    browser = webdriver.Firefox()

browser.get('https://inventwithpython.com')


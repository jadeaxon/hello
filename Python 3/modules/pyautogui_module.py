#!/usr/bin/env python3

# PRE: pip3 install pyautogui

# FAIL: pyautogui does not work from Cygwin
import sys
if sys.platform == 'cygwin':
    print("ERROR: pyautogui does not work in Cygwin.")
    sys.exit()

import pyautogui as pag

screen_size = pag.size()
print(screen_size)

pag.moveTo(100, 100, duration=0.3)

pos = pag.position()
print(pos)
print(pos.x)
print(pos.y)

pag.click()
pag.click(100, 100)
# pag.click(100, 100, button='right')

pag.mouseDown()
pag.mouseUp()

# pag.drag()
# pag.scroll()

# Kind of like the AHK Window Spy.
# Meant to be called by itself so you can plan what your automation script needs to do.
# pag.mouseInfo()

# Pixel scraping.
# image = pag.screenshot()
pixel = pag.pixel(100, 100)
print(pixel)

# Search for an image on screen. Unfortunately, has to be a perfect match.
# box = pag.locateOnScreen('button.png')

# pag.click('button.png') # Shortcut to find and click on what looks like a button.


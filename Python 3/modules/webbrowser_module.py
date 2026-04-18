#!/usr/bin/env python3

# WARNING: If you name this file webbrowser.py it fails due to a circular module import.

import sys
if sys.platform == 'cygwin':
    import os
    os.environ['BROWSER'] = 'cygstart'

import webbrowser

webbrowser.open("http://www.google.com")


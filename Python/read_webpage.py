#!/usr/bin/env python

import urllib2

# Print out the HTML source of the Google homepage.
for line in urllib2.urlopen('http://www.google.com'):
    print line


#!/usr/bin/env python

# A few libraries that may be useful for HTML scraping.
# urllib2
# BeatifulSoup
# Scrappy
# Mechanize

import urllib2 # Allows you to access URLs.
import re # Regular expressions.


# We are in the region of the file that has actor names.
inActors = False

# Fetch a web page.
url = 'http://www.imdb.com/title/tt0133093/' # The Matrix
response = urllib2.urlopen(url)

# Let's try to extract the main actors for this movie.
# The response is "file-like" so should be able to iterate over it.
# You can extend the concepts here to eventually extract all interesting info from the file.
for line in response:
	# print line

	line = line.strip()
	line = line.rstrip('\n')
	# print line
	if line == '<h4 class="inline">Stars:</h4>': 
		print "webbot: In actors zone."
		inActors = True

	# fullcredits
	if inActors and ("fullcredits" in line): inActiors = False

	# We are parsing lines that may contain actor names.
	# <a href="/name/nm0000206/?ref_=tt_ov_st" itemprop='url'><span class="itemprop" itemprop="name">Keanu
	# Reeves</span></a>,
	if inActors:
		if line.startswith('<a href="/name/'):
			# Regular expressions are one of your best friends in life.
			# Strip HTML tags.  Then delete all trailing commas.
			actor = re.sub('<[^<]+?>', '', line)
			actor = re.sub(',+$', '', actor)

			# Clean up a bit.  My parsing isn't super refined.
			actor = actor.strip()
			actor = actor.strip('\n')
			if actor: print actor

			# TO DO: Remove duplicates from the list of actors.
		# if
	# if
# next line



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
inGenres = False
inRuntime = False
inSynopsis = False
genres = []
actors = []

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

#----------------------------------------------------------
# Extract Title
        if line.startswith('<h1 class="header"> <span class="itemprop" itemprop="name">'):
                print "webbot: In title zone."
                title = re.sub('<[^<]+?>', '', line)
                title = title.strip()
                print title
#----------------------------------------------------------
# Extract Rating
        if line.startswith('itemprop="contentRating" content='):
                print "webbot: In rating zone."
                rating = re.sub('itemprop="contentRating" content="', '', line)
                rating = re.sub('"></span>', '', rating)
                print rating
#----------------------------------------------------------
# Extract Runtime
        if line == '<h4 class="inline">Runtime:</h4>':
                print "webbot: In runtime zone."
                inRuntime = True
        if inRuntime and ("</div>" in line): inRuntime = False
        if inRuntime and line.startswith('<time itemprop="duration"'):
                runtime = re.sub('<[^<]+?>', '', line)
                runtime = runtime.strip()
                print runtime
#----------------------------------------------------------
# Extract Genres
        if line == '<h4 class="inline">Genres:</h4>':
                print "webbot: In genres zone."
                inGenres = True
        if inGenres and ("</div>" in line): inGenres = False
        if inGenres and line.startswith('<a href="/genre/'):
                genre = re.sub('<[^<]+?>', '', line)
                genre = re.sub('&nbsp;', '', genre)
                genre = re.sub(r'\|', '', genre)
                genre = genre.strip()
                genres.append(genre)
                print genre
#----------------------------------------------------------
# Extract Synopsis
        if line == '<p itemprop="description">':
                print "webbot: In synopsis zone."
                inSynopsis = True
        if inSynopsis and ("<p></p>" in line): inSynopsis = False
        if inSynopsis and line != '<p itemprop="description">':
                synopsis = re.sub('<[^<]+?>', '', line)
                synopsis = synopsis.strip()
                print synopsis
                if len(synopsis) > 250: print "webbot: ***Warning! IMDb's synopsis exceeds 250 chars and will need to be revised!"
                else: print "webbot: ***IMDb's synopsis is 250 chars or less, and is therefore suitable to import directly!"
#-----------------------------------------------------------
# Extract Actors
        # print line
        if line == '<h4 class="inline">Stars:</h4>': 
                print "webbot: In actors zone."
                inActors = True

        # fullcredits
        if inActors and ("fullcredits" in line): inActors = False

        # We are parsing lines that may contain actor names.
        # <a href="/name/nm0000206/?ref_=tt_ov_st" itemprop='url'><span class="itemprop" itemprop="name">Keanu
        # Reeves</span></a>,
        if inActors:
                if line.startswith('<a href="/name/'):
                        # Regular expressions are one of your best friends in life.
                        # Strip HTML tags.  Then delete all trailing commas.
                        actor = re.sub('<[^<]+?>', '', line)
                        actor = re.sub(',+$', '', actor)
                        actor = re.sub(r'\|', '', actor)

                        # Clean up a bit.  My parsing isn't super refined.
                        actor = actor.strip()
                        actor = actor.strip('\n')
                        if actor:
                                actors.append(actor)
                                print actor
                # if
        # if
#------------------------------------------------------------
# Export data to a text file - yes, the line numbers are explicit
print 'webbot: Exporting data to digEcor standard synopsis textfile...'
filename = re.sub(r'\s', '', title) + '.txt'
f = open(filename, 'w') # Make a new file in output mode

line1 = title
line2 = rating + ' / ' + runtime
line3 = ''
for genre in genres:
        line3 = line3 + genre + " / "
line3 = re.sub(' / +$', '', line3)
line4 = ''
for actor in actors:
        line4 = line4 + actor + ", "
line4 = re.sub(', +$', '', line4)
line5 = synopsis

f.write(line1 + '\n')
f.write(line2 + '\n')
f.write(line3 + '\n')
f.write(line4 + '\n')
f.write(line5 + '\n')

f.close( )
print 'webbot: Export complete!'
#-------------------------------------------------------------
# END WEBBOT
#-------------------------------------------------------------

#!/usr/bin/env python

import os

# We'll split out this path into its directory, filename, and extension components.
path = "/home/jadeaxon/junk.tar.gz"

directory, filename = os.path.split(path)
basename = os.path.basename(path)
name, extension = os.path.splitext(filename)

# Does not include a trailing /.
print "directory: %s" % directory

# These two values are the same.
print "filename: %s" % filename
print "basename: %s" % basename

# Includes the dot.
# Does not handle double extensions like .tar.gz properly.
print "name: %s" % name
print "extension: %s" % extension

# It's tricky to generally extract extensions because you might have file names with version numbers in
# them that use dots.
# You could say that the last n dot separated chunks where the chunk is not all digits.  That would get you
# something like foo.1.27.tar.gz correctly.  Most meaningful extensions do not consist of just numbers.



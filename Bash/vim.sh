#!/usr/bin/env bash

# Apply a Vim script (in a here document) to each commandline arg.
# That is do batch editing in Vim.  More like sed or perl -p -i -e.
for file in "$@"; do
	# Vim always treats stdin as a file to edit whereas ex treats stdin as commands.
	# FAIL: vim -e - $file <<- END_OF_SCRIPT # Of all things, this *should* work.
	# exim is Ex Improved.  It's all really Vim in the end.
	# Problem is exim is also some kind of mail application in Cygwin.
	# FAIL: exim - $file <<- END_OF_SCRIPT
	# FAIL: vim -E - $file <<- END_OF_SCRIPT
	# FAIL: vim -s "-" -- $file <<- END_OF_SCRIPT
	# FAIL: vim -e -s - $file <<- END_OF_SCRIPT
	# WIN: ex - $file <<- END_OF_SCRIPT
	vim -E $file <<- END_OF_SCRIPT
		g/\<their\>/s//their/g
		g/\<writable\>/s//writable/g
		wq
	END_OF_SCRIPT
done # next file

# Should fix _thier_ and _writeable: their writable. 



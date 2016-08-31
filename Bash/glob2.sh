#!/usr/bin/env bash

# Usually, when no match, glob expands to itself literally.
# This is generally not what you want.
echo nullglob off: *nomatchy*

# Generally, you want nullglob on!
shopt -s nullglob
echo nullglob on: *nomatchy*
shopt -u nullglob

# You can do recursive globs like in Ant.
# You must set globstar.  It is not inherited from parent process.
shopt -s globstar
echo **
echo

# You can loop over them.  This correctly handles paths with spaces.
for f in **; do
	echo "$f"
done
echo

# You can use globs with alternation.  Alternation is expanded first.
ls -la hello_{a,b,c}*.sh
echo


# By default, * and ? do not match files starting with a dot.
# You can use .* or .? to explicitly see them.  Or set dotglob shell option.
# shopt -s dotglob
ls --color=auto -lad .* *
echo

# Suppose you need to remove a file named '?*'.
# Use backslashes to escape metachars (turning them back into normal chars).
ls -la \?\*
echo



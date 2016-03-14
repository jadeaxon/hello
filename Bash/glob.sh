#!/usr/bin/env bash

# Expand empty globs to single null string (instead of the glob itself).
shopt -s nullglob
set -e # Die on first error.

S=$(basename $0) # This script.
D=$(pwd) # The directory from which this script was invoked.

# Expand glob using a subshell.
glob=glob.* # NOTE: The glob will not expand on assignment.
# WARNING: nullglob won't be on in the subshell, so better to expand in this shell.
expanded_glob=$(echo $glob)

# Expand glob without using a subshell.
expanded_glob=( $glob ) # Expand glob into an array.
expanded_glob=${expanded_glob[0]} # Get just the first array element.

# Should output glob.sh.
echo $expanded_glob




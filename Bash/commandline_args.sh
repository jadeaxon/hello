#!/usr/bin/env bash

# The commandline arguments are known as 'positional parameters'.
# The are accessible via special shell variables $1 to $9.
# Argument 10 and above must be brace enclosed: ${10}, etc.
# $0 is the program name (as invoked on the commandline).
# So, it will be a relative or full path, but never a pure basename.

# If you need to process commandline options/switches, you may want to look into the getopts bash command.

# The getopts built-in only supports short options (single letter).
# You need an external command or library to handle long options.

program_name=$(basename "$0")

echo '$0' == $0 "(program name: $program_name)" 
echo '$1' == $1 '(first positional argument)'
echo '$2' == $2
echo '$3' == $3
echo '$4' == $4
echo '$5' == $5
echo '$6' == $6
echo '$7' == $7
echo '$8' == $8
echo '$9' == $9
echo '${10}' == ${10}
echo

# The simplest validation is whether an arg string is undefined, empty, defined, or non-empty.

# Use Bash's default-without-setting-allowing-empty-strings mechanism to check if a variable is undefined.
if [ -z "${1+default}" ]; then 
	echo '$1 is not defined.'
fi

# Check if $1 is undefined or a null string.
# Be sure to use the double quotes around the arg else you get a syntax error if arg is not defined.
if [ -z "$1" ]; then
	echo '$1 is either undefined or an empty string.'
fi

# The default operator for [ ] is unary -n.  This returns success its string arg is non-empty.
if [ "$1" ]; then # Same as if [ -n "$1" ].
	echo '$1 is defined and not an empty string.'
fi

echo

# Loop through the commandline args with a for loop.
echo "for loop:"
for argument in "$@"; do 
  echo $argument

done 
echo

# Also loops through the commandline arg with a for loop.
# More concise, but confusing if the first time you've seen it.
echo "for loop:"
for arg; do
	echo $arg
done
echo

# The value of $# is the number of commandline arguments.  
echo "while loop:"
while [ $# -gt 0 ]; do 
  echo $1 
  shift # Pop the argument stack.  $2 becomes $1, etc.

done 
echo






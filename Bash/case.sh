#!/usr/bin/env bash

# A bash case switch.
# Each case value ends with ')'.
# The ;; prevent fallthrough.
# The * case is the default "everything else" handler.
# Bash uses the odd reversed keyword closing pair 'esac'.
case "$1" in
    one)
        echo 1 
        ;;
    two)
        echo 2
        ;;
    three)
        echo 3
        ;;
    *)
        echo "Unrecognized argument."
        ;;
esac                                      


# case word in [ [(] pattern [| pattern]...) command-list ;;]... esac
#
# The first pattern matching <word> (reading top-to-bottom/left-to-right) triggers its command list.
# The patterns appear to be glob patterns.
# A list of patterns can be or'd together with |.  Match any => trigger command list.
# Various expansions are performed on <word> and <pattern> before matching occurs.
# The optional leading ( appears to be meaningless.
#
# ;; => stop at first match
# ;& => fall through and execute next command list unconditionally
# ;;& => fall through and keep checking for next pattern match

# Do case-insensitive pattern matches.
shopt -s nocasematch


# Check that two commandline arguments were given.
# Note that an individual case can span multiple lines.
case $# in 
    2) ;; # We need 2 args, so do nothing. 
    *) printf "%s\n" "Please provide two arguments." >&2 # Print to stderr. 
       exit 1 
       ;; 

esac


# Bash case switches select the branch where the query argument matches a glob pattern.
# <pattern> <commands> ;;
# Not sure why you need two semicolons.
#
# This tests if commandline arg 2 is contained within commandline arg 1.
# Returns 0 (true) if so, and 1 (false) otherwise.
case $1 in 
    *"$2"*) true ;; 
    *) false ;; 

esac 


read -p "Enter a word: " 
printf "'$REPLY' "
case $REPLY in 
	[[:alpha:]])
		echo "is a single alphabetic character." ;; 
	[ABC][0-9])
		echo "is A, B, or C followed by a digit." ;; 
	???)
		echo "is three characters long." ;; 
	*.txt)
		echo "is a word ending in '.txt'" ;; 
	*)
		echo "is something else." ;; 
esac












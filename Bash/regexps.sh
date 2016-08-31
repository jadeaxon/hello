#!/usr/bin/env bash

# Regular expressions can *only* be used within a [[ command.
# They are Perl-compatible (?).
# regexp='^.*$'
# [[ "$string" =~ "$regexp" ]]

string="This is a test string to match against."
regexp='(match)'

# The test does match on a partial match.
# WARNING: The crazy thing is that you cannot say "$regexp" or else ()s will cause the match to fail.
# You must just use $regexp with no quotes.  So use \s instead of a space in the regexp.
if [[ "$string" =~ $regexp ]]; then
	echo "Match!"
fi


# If the number of commandline args is less than 2, print the usage message.
# $0 - the name of this script.
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 PATTERN STRINGS..."
	echo "You must use \( and \) for grouping because ( and ) have special meaning to bash."
    exit 1
fi


regexp="$1" # You can't put extra space around the =.
shift # Next argument is now $1.
echo "regexp: $regexp"
echo


# Try to match regexp against each argument.
while [[ "$1" ]]; do
	# Checks to see if $regexp partially matches current arg, $1.
    if [[ "$1" =~ $regexp ]]; then
        echo "Pattern $regexp partially matches $1."

		# List all the parentheses group submatches.
        i=1
        n=${#BASH_REMATCH[*]} # Number of paretheses group submatches.
        while [[ $i -lt $n ]]; do
            echo "  capture[$i]: ${BASH_REMATCH[$i]}"
            let i++
        done # next subgroup
    else
        echo "Pattern $regexp does not match $1 at all."
    fi

    shift # next arg

done # next regexp comparison


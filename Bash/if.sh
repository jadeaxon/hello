#!/usr/bin/env bash

# This is how you set a variable.
myvar="$1"
echo $myvar

# Test for emptiness.
if [ -z "$myvar" ]
then
    echo "myvar is not defined"
    exit 1
fi

# Test for equality.
# It's always safest to surround your variable dereferences with double quotes.  Handles whitespace correctly.
if [ "$myvar" -eq 3 ]
then 
    echo "myvar equals 3"
fi

# Test for equality.
if [ "$myvar" = "3" ]
then
    echo "myvar equals 3"
fi


# This is how you set a variable.
myvar="$1"
echo $myvar

# Test for emptiness.
if [ -z "$myvar" ]
then
    echo "myvar is not defined: Please supply an integer commandline argument."
    exit 1
fi

# Test for equality.
# It's always safest to surround your variable dereferences with double quotes.  Handles whitespace correctly.
# Bash will complain if myvar is not an integer.
if [ "$myvar" -eq 3 ]
then 
    echo "myvar equals 3"
fi

# Test for equality.
if [ "$myvar" = "3" ]
then
    echo "myvar equals 3"
fi

# Looks like the if syntax is a bit funky and unforgiving.
if [ 3 -eq 3 ]
then
    echo "Typically, keyword 'then' must be on separate line."
fi

#if [ 3 -eq 3 ] then
#    echo "then can be on same line as if"
#fi


# The alternate syntax to get if and then on the same line uses a semicolon.
if [ 3 -eq 3 ]; then
	echo "With alternate syntax, if and then are now on the same line."
fi


# if/else if/else
echo
printf "Enter a number between 10 and 20 inclusive: " 
read number 
if [ "$number" -lt 10 ]; then 
    printf "%d is too low.\n" "$number" >&2 
    exit 1 

elif [ "$number" -gt 20 ]; then 
    printf "%d is too high.\n" "$number" >&2 
    exit 1
 
else # The number is in the right range. 
    printf "You entered %d.\n" "$number" 

fi


# To make if statements that are more like C, use arithmetic context (( )).
# Arithmetic context use C integer truth: 0 => false; !0 => true.
# Also, in arithmetic context you use the normal C operators like < rather than -lt.
if (( 0 )); then
	echo "0 is true in arithmetic context."
fi

if (( 1 )); then
	echo "1 is true in arithemetic context."
fi

if (( $# > 1 )); then
	echo "Extra commandline arguments were passed in."
fi



#!/usr/bin/env bash

# Generate 9 random numbers.  Only print the ones >= 20,000.
for n in {1..9} # This is 'brace expansion'. 
do 
	x=$RANDOM 
	[ $x -le 20000 ] && continue 
	echo "n=$n x=$x" 

done

# Like break, continue can also be given an integer argument to tell it how many levels of looping to jump out of.



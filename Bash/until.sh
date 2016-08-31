#!/usr/bin/env bash

# until <command>; do <command>...; done

# <command>... is ;-separated.
# You can subs \n for ; or not.

# An until loop always executes the loop body once.
# This is the only difference between it and a while loop
# It is the same thing as a do-while loop in other languages.

# Count from 0 to 9.
i=0
until [ $i -eq 10 ]; do
    echo $i
	(( i++ ))
done


n=1 
until [ $n -gt 10 ]; do 
	echo "$n" 
	# n=$(( $n + 1 ))
	(( n++ ))

done

 

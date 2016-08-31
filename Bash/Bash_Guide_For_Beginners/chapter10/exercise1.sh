#!/usr/bin/env bash

# Print out all the commandline args.n
echo "argv[0]: $0"
i=1
while [ "$1" ]; do
	echo "argv[$i] == " $1
	# Shift only shifts the positional args: $1, $2, ...
	# Does not affect $0.
	shift 

	(( i++ ))
done

(( i-- ))
echo "Total positional args: $i."



#!/usr/bin/env bash

# Otherwise pipelines succeed if just their last command exits 0.
set -o pipefail 

S=$(basename $0)

if gcc -std=c11 main.c |& tee make.out; then
	rm make.out
	if [ -x a.out ]; then # Linux
		./a.out
	elif [ -x a.exe ]; then # Cygwin 
		./a.exe
	else # No executable found.
		echo "$S: ERROR: No executable found!"
		exit 1
	fi
else # Compilation failed.
	# Edit errors as a Vim quicklist.
	vim -q make.out
fi



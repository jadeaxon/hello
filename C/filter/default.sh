#!/usr/bin/env bash

set -o pipefail

# This script is triggered by . alias which calls do_default_action(). 
# This mechanism is defined in by .bashrc via my bash-glory lib.

# Compile and run the most recently modified .c file.
last_modded=$(ls -1t *.c 2> /dev/null | head -1)
if [ -z "$last_modded" ]; then
	ls -lahF --color
	exit 0
fi

if gcc -Werror $last_modded |& tee make.out; then
	./a.out
else
	vim -q make.out
fi


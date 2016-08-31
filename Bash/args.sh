#!/usr/bin/env bash

echo Script: $0
echo First commandline argument: $1
echo Second commandline argument: $2 
echo All commandline arguments: $@
echo Number of commandline arguments: $#
echo

# List all the commandline arguments.
for argument in "$@"
do
    echo Argument: ${argument}
done



#!/usr/bin/env bash

# There are two forms of the for loop:
# for name [ [in [words ...] ] ; ] do commands; done
#
# for <var> in <word>...; do <command>... ; done
#
# <word>... is space-separated (IFS).
# <command>... is ;-separated.
#
# If 'in words' is omitted, it defaults to 'in "$@"', that is, the positional args.
# A newline can be used instead of a semicolor anywhere.  Use ; for one-liners.
#
# Alternations, globs, and $(command expansions) are good ways to provide a list or words for a for loop
# to operate on.
#
# for (( <expr1> ; <expr2> ; <expr3> )) ; do <command>... ; done
# This is like a C for loop.

# I/0 redirection (including piping) can be applied to the entire for construct.
# Not sure how you'd usefully pipe into a for loop though.

# You can use 'break' and 'continue' inside loops.
# I don't think there are labelled loops, but I think you can say 'break 2' to exit two loop layers.


# Assign x to each element in the list iteratively.
for x in one two three four
do
    echo element $x
done
echo

# Another example of 'for variable in list' syntax.
for var in Canada USA Mexico; do 
	printf "%s\n" "$var" 
done 
echo 


# Use two globs to define a list of paths to iterate over.
# You can use one or more globs.
# The globs can use absolute or relative paths.
# You probably want 'shopt -s nullglob'.
# Also, beware of when the filenames contain spaces. 
# Probably double-quoting the glob will work.
#
# Check if each one is a directory.
for file in /etc/r* /etc/s*; do
    if [ -d "$file" ] 
    then
        echo "$file (directory)"
    else
        echo "$file (file)"
    fi
done
echo


# Uses backticks for command execution.
# Notice how slow it is to launch a process to deal with each element.
# basename gets just the name.ext of a file with no directory information.
# NOTE: It is better to use the $() syntax instead of backticks.  Easier to read.
for x in /var/log/*; do
    echo `basename $x` is a file living in /var/log
done
echo

 
# Non-standard syntax similar to C for loops. 
# The three expressions are evaluated using bash arithmetic evaluation, as if
# they were inside $(( )).
for (( n = 1; n <= 10; ++n )); do 
	echo "$n" 
done 
echo

for (( n = 1; n <= 10; n++ )); do
	echo "$n"
done
echo


file=$0
echo "File: $0"

# One liner to count the words in a file.
# Of course, using the wc program is better.
# ${n:-0} uses value of n if n is set, otherwise 0.
for word in $( cat "$file" ); do n=$(( ${n:-0} + 1 )); done
echo "Word count: $n"

# Read first four lines of a file into an array of lines.
# Using brace expansion (alternation) to generate word list.
declare -a lines
for n in {1..4}; do
	echo "Reading line $n from $file into array 'lines'."
	read lines[$n]
done < "$file"
echo "lines[1] == " ${lines[1]}
echo


# Create some random, zero-length files.
for file in {a..z}$RANDOM.junk; do 
	> "$file" 
done


# Loop over a sequence a floating point values.
# The external seq command can generate such a sequence.
for float in $(seq 1.0 .01 1.1); do
    echo $float
done


# Loop over all the files in current directory subtree.
# This does handle filenames with spaces in them.
# Demonstrates that Bash can do recursive globs (like in Ant).
for f in **; do
	echo "$f"
done




#!/usr/bin/env bash


# while <command>; do <command>...; done

# <command>... ;-separated
# Any ; can be replaced by a newline (or not).

# while true; do echo "Are we there yet?"; sleep 1; done

# Count from 0 to 9.
# In bash, you cannot put extra space around your assignments (which is lame).
# i = 0 is not valid; bash sees i as a command name and can't find it
i=0
while [ $i -ne 10 ]; do
    echo $i
    i=$(( $i + 1 ))

done
echo

# Same thing.
i=0
while (( i != 10 )); do
	echo $i
	(( i++ ))
done
echo


# Count from 1 to 9.
n=1 
while [ $n -le 10 ]; do 
  echo "$n" 
  # $((<expression>)) is bash arithmetic expression substitution syntax.
  n=$(( $n + 1 ))

done 
echo 


# IFS is the interfield seperator.  Setting it to nothing causes entire lines to be read.
# By using -r, space within the line is preserved instead of being cooked down to single spaces.
# You can list variable assignments that will apply to a command on the same line before it in bash.
# So, this loop reads each line from this file, $0, and prints it back out with 'code: ' prefixed.
# The redirection happens on the done line because you could write the while loop as a one-liner
# using ; instead of \n.
while IFS= read -r line 
do 
	echo code: $line
done < $0
echo

# while IFS= read -r line; do eCho code: $line; done < $0


# The true command can be used to create an infinite loop.
# true is a built-in command which returns 0; false is a built-in command which returns 1. 
# : is a no-op which returns 0; thus it can be used in place of the true command.
echo 'Press <Ctrl + C> to exit.'
while true; do 
  read x
  echo Read: $x

done


something() {
	: # Blocks in Bash must contain at least one statement.
}


# One liners to process lines from multiple files.
cat *.txt | while read line; do something $line; done 
 
# The same thing can be done using process substitution.  The advantage of using process substitution is that variables modified 
# within the while loop will be visible to the rest of the script.  The disadvantage is that it makes the script less portable. 
while read line; do something $line; done < <(cat *.txt)

# Infinite loops.
echo "Press ^C to break from infinite loop."
while true; do
	:
done


# Arithmetic context inverts its result, so you end up with C-style logic.
echo "Press ^C to break from infinite loop."
while (( 1 )); do
	:
done

	











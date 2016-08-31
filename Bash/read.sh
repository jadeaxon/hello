#!/usr/bin/env bash

# The read builtin reads a line from stdin.
# It's args are variable names.
# It tokenizes the input line by IFS.
# It stores each token in the arg variables in order.
#
# If more tokens than variables, all excess tokens joined via a single space to last assigned
# variable.  So, the last token gets all remaining stuff, but literal whitespace not preserved.
# 
# Thus, if you use read with a single arg, the whole line gets assigned to that variable with
# leading/trailing whitespace stripped and inter-token whitespace compressed to a single space.
# Note that the trailing \n is stripped too.
#
# To read a literal line, set IFS='' and read into a single variable.


# read [options] <name1> ... <nameN>

echo "Enter a line:"
read token the_rest
echo $token
echo $the_rest
echo

# If you specify no arg to read, it is implicitly uses REPLY as the only arg.
# -p means prompt
read -p "The string you enter will be stored in REPLY: "
set | grep ^REPLY
echo

# -p option lets you specify a prompt
# However, it does not emit a newline, and \n does not work.
# If you want a prompt with a newline, just use echo before read as shown above.
read -p 'How old are you? ' age
if (( age < 35 )); then
	echo "You know nothing!"
else
	echo "You must be very wise."
fi
echo


# The -t <seconds> option lets you set a timeout.
read -t 5 -p 'You have 5 seconds to tell me your name: ' answer
if (( $? == 0 )); then # $? is exit status of last command.  0 => success.
	echo "You are quick, $answer."
else
	echo # Since we get no newline from user input.
	echo "Too slow."
fi
echo

# You might think you could use
# if return $?; then ... above.
# You can't: return can only be called from a function or from a sourced script.


# You can set read to accept a specific number of characters instead of waiting for newlines.
# This can give you video game like single keystroke processing.
#
# Notice that the key you press is still echoed to the screen.
# To disable this, use the -s option of read.  It means 'silent'.
echo "Welcome to q => quit!"
silent=""
while :; do
	read $silent -n1 keystroke
	if [ "$keystroke" == "q" ]; then
		echo 'q => quit!'
		break
	fi

	if [ "$keystroke" == "s" ]; then
		silent='-s'
	fi

	if [ "$keystroke" == "v" ]; then 
		# Verbose.
		silent=''
	fi

	echo "You pressed '$keystroke'."
done
echo


# Since read reads from stdin, you can use it with pipes or redirection.
# Thus, you can read from files.

OLD_IFS="$IFS"
IFS=$'\n' # This should allow us to preserve whitespace in each line.
head $0 | \
while read line; do
	echo "$line"
done
IFS="$OLD_IFS"
echo


# Read input one character at a time.
# Actually, the input is read one line at a time, but then processed character by character.
# The newline does not appear to be contained within $line.
echo "Is there an echo in here?"
while read line; do
    for ((i=0; i < ${#line}; i++)); do
        character=${line:i:1}
        printf "%s" $character

    done
	echo

done




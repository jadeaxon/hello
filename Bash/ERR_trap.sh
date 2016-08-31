#!/usr/bin/env bash

# Demonstrates how to run a command and get its exit status when a global error handler trap is
# active.

error_handler() {
	echo "error_handler()"
	# Yes, if you don't exit here, execution will continue on the line after line that had error.
	exit 2
}
trap 'error_handler' ERR


# Executes in a subshell.  Returns its exit status.
# This allows you to get the exit value of a command w/o triggering the error trap in main script.
subshell_function() {(
	trap 'return' ERR
	false
	echo Hi
)}

echo "This script will blow up to ERR handler on nonzero exit."
subshell_function
echo "Exit value of subshell_function() is $?." # This reports correctly.
false # This will trigger error handler.

# This line *will* execute if error_handler() does not exit script.
echo "This line executed after error_handler()."

exit 0




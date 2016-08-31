#!/usr/bin/env bash

# Example of how to trap signals in bash.
# Signals are essentially high-level interrupts.

# Other than perhaps environment variables, signals are one of the most basic forms of interprocess communication (IPC)
# available.

# A signal is like a zero-arg method call from one process to another.

# Generally, you don't want signal handlers to do much.
handle_signal() {
	# This message will appear on the terminal where this script is running.
	# It will not appear on the terminal from where the signals are sent.  Unless same terminal.
	printf "Caught $1 signal.\n"
}

# The general syntax for trap is
# trap "<command>" <signal>...

# This is not a complete list of signals.
# The trap built-in lets you register a command to be called when the script's process is signalled.
trap "handle_signal ABRT" ABRT
# EXIT is a bash pseudo signal.  The script receives this right when it exits.
trap "handle_signal EXIT" EXIT
trap "handle_signal HUP"  HUP
trap "handle_signal INT"  INT
# You can't actually trap KILL.  The kernel receives it and acts on the target process.
trap "handle_signal KILL" KILL
trap "handle_signal QUIT" QUIT
trap "handle_signal TERM" TERM
trap "handle_signal USR1" USR1
trap "handle_signal USR2" USR2


# This is how you remove a trap (unregister a signal handler).
# When the trap is removed, the default trap is restored.  The signal is not simply ignored.
# The default response to this signal is for the program to exit.
trap - USR2

# I believe a child process inherits the signal handlers of its parent (?).


# Open another terminal and use 'kill' to send signals to the reported process id.
echo $$

while (( 1 )); do
	: # Wait for signals.

	# sleep is not a built-in, so if you use it here, the script will not be interruptible while the external sleep
	# command is running.  The signal will be handled after the sleep finishes.
	sleep 1

	# Not sure if this kind of loop results in a busy wait.
	# It is a complete busy wait in Cygwin.  CPU hits 100%.
done







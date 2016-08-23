#!/bin/bash

# The child process just writes its .pid file and waits forever.
# The parent calls this as a background process, disowns it, and kills it.

# When a child process dies, the OS sends SIGCHLD to its parent.
# Note that job control and process control are not the same things.
# Jobs only exist at the shell level.  Processes exist at the kernel level.

pidf=/var/run/child.pid
rm -f $pidf
echo $$ > $pidf

while true; do
	sleep 1
done


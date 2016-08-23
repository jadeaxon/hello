#!/bin/bash

# Without this, the reaper() trap will not trigger at all. 
# It's not clear to me why enabling job control allows me to trap SIGCHLD.
set -o monitor

# FAIL: Even trapping SIGCHLD or disabling the trap cannot eliminate this output:
# ./parent.sh: line 25: 16209 Terminated              ./child.sh
# Seems there's some built-in SIGCHLD handler or job control stuff that can't be disabled by these
# means if at all.
reaper() {
	echo "Reaping child process."
}
trap 'reaper' CHLD
# trap - CHLD

S=$(basename $0)
echo "$S: Starting child.sh"
./child.sh &
disown
# NOTE: This does *not* make child.sh not a child process of this process.  Thus it will trigger
# the SIGCHLD trap.  What disown does is remove the call as a *subjob* in job control.

sleep 5

echo "$S: Killing child.sh"
pidf=/var/run/child.pid
pid=$(cat $pidf)

# The other option would be to have the child process trap SIGINT and clean up its own .pid file.
if [ -f $pidf ]; then
	kill $pid
	rm -f $pidf
fi
echo "$S: Done."








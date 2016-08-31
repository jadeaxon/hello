#!/usr/bin/env bash

# This script prints a few interesting tidbits of information about your shell environment.

# Prints your home directory.
echo $HOME
# Prints your terminal type.
echo $TERM

# Prints system services that should start for runlevel 3.
# In Cygwin, there are none.
service_dir='/etc/rc3.d'
if [ -d "$service_dir" ]; then
	ls -la $service_dir/S*
else
	echo "WARNING: $service_dir does not exist on this machine."
fi

exit 0


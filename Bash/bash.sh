#!/bin/bash

#: Title       : hello_bash.sh 
#: Date        : 2011-12-14 
#: Author      : Jeff Anderson
#: Version     : 1.0 
#: Description : print Hello, bash! 
#: Options     : None 

# Note that the echo command will expand a glob if possible.
# However, if the glob does not expand, it will print the literal glob characters.

# Print fully expanded command before executing it.  Prefix the line with $PS4.
set -o xtrace

echo "Hello, bash!"
printf "%s\n" "Hello, bash!" 

echo "\$HOSTNAME = $HOSTNAME"



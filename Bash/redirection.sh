#!/usr/bin/env bash

# Generally stdout and stderr of a process are connected to a terminal device (driver).
# Since a terminal is a character device, it can accept such a stream of characters.

# stdin of a process is connected to the keyboard device.

# Instead of connecting to a terminal device or a keyboard device, you might just want to send these
# character streams to a file or read them from a file.  That's redirection.

# Print a single message to stderr instead of stdout.
echo "Error message." >&2

# To discard output, send it to the bit bucket, /dev/null.
echo "I'm melting!" > /dev/null

# The three standard file descriptors are
# 0 - stdin
# 1 - stdout
# 2 - stderr

# You can use 0..8 in your scripts.  Thus, 3..8 can be used for whatever you want.
# This will cause anything you write to file descriptor 3 to go to the file three.txt.
exec 3> three.txt
echo "A line of text for three.txt." >&3

# Send the output character stream to a file instead of stdout.
echo "Character stream." > output.txt

# Append to the file instead of overwriting it.
echo "Character stream." >> output.txt

# Direct both stdout and stderr to same file.
echo "Character stream." >& output.txt # Syntax borrowed from csh.
echo "Character stream." &> output.txt
echo "Character stream." 1> output.txt 2> output.txt

# Direct stdout and stderr to different files.
echo "Character stream." 1> stdout.txt 2> stderr.txt


# Make stdin read from a file instead of from the keyboard device.
touch input.txt
echo "A line from input.txt." >> input.txt
cat < input.txt

# Permanently redirect all future stdin from a file.
# What happens when input is requested but EOF reached?  Does program just wait forever?
# No, it does not hang.  Looks like it just returns empty strings.
# Perhaps the exit status of read is non-zero?
# The read fails both times and does not even print the prompt (when input file empty).
# It appears that read -p only prints a prompt if stdin is a keyboard device.
# Regardless of what stdout is directed to.
# Yup, this is exactly what is happening.  I verified in a small test script.
exec 0< input.txt

read -p "Need input: " line
echo $?
read -p "More input: " line
echo $?

# How do we set file descriptor 1 (stdout) back to the terminal driver?
# First, save current stdout to another file descriptor.
exec 4>&1

# Permanently redirect all future stdout output of this script to a file.
exec 1> redirection.log
echo "Now stdout will go to the log file."

# Now, restore stdout (file descriptor 1) to what it was.
exec 1>&4
echo "This will now print to the terminal, not the log file."


# You can create a read/write file descriptor. 
# Not sure why you would ever want to.  Be careful if you do.
exec 5<> output.txt

# To close a file descriptor, redirect it to special location &-.
exec 5>&-







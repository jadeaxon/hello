#!/usr/bin/env bash

# Set S to just the name of this script ($0 can contain path info).
S=$(basename $0)

# Use getopt to check positional args and rearrange/expand them for easier option processing
# in the loop below.
ARGS=$(getopt -ovh --long verbose,help -n "$S" -- "$@")
if (( $? != 0 )); then
	echo "$S: ERROR: One or more invalid options were detected."
	exit 1
fi
eval set -- "$ARGS"

helpopt=0
verboseopt=0

# Now go through all the options.  These have been validated to some degree by getopt
# and preprocessed so they'll be found in the loop below.
while true; do
    case "$1" in
        -v|--verbose) 
			echo "--verbose"
			verboseopt=1 # Set a global var to indicate --verbose was on the command line.
			shift # $2 is now $1, etc.  That is, process the next command-line arg.
			;;
        -h|--help) 
			echo "--help"
			helpopt=1 
			shift
			;;
        --) 
			shift 
			break
			;;
    esac
done

echo $helpopt
echo $verboseopt


# Prints args to stdout if --verbose option is set.
echov() {
	if (( verboseopt )); then
		echo "$@"
	fi
}

echo "This will always be echoed, even if --verbose option is not set."
echov "The --verbose option was set."
exit 0




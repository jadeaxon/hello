#!/usr/bin/env bash
# hello_color.sh: Echoing text messages in color.

# Define ANSI escape sequences for colors.
# 2nd number 40 => black background.
# See http://en.wikipedia.org/wiki/ANSI_escape_code.
# Basically escape code 30-37 set foreground color.  40-47 set background color.
black='\E[30;40m'
red='\E[31;40m'
green='\E[32;40m'
yellow='\E[33;40m'
blue='\E[34;40m'
magenta='\E[35;40m'
cyan='\E[36;40m'
white='\E[37;40m'



# Echoes colorized text.                             
# $1: message
# $2: color
cecho () {
	local default_msg="No message passed."
								# Doesn't really need to be a local variable.

	message=${1:-$default_msg}   # Defaults to default message.
	color=${2:-$black}           # Defaults to black, if not specified.

	echo -e "$color"
	echo "$message"
	tput sgr0 # Reset the tty.

	return
} # cecho() 


# Main.

cecho "Yellow banana." $yellow
cecho "White knight." $white
cecho "Feeling blue..." $blue
cecho "Magenta looks more like purple." $magenta
cecho "Green with envy." $green
cecho "Seeing red?" $red
cecho "Cyan, more familiarly known as aqua." $cyan
# cecho "No color passed (defaults to black)."
# cecho "\"Empty\" color passed (defaults to black)." ""
# cecho
# cecho "" ""

echo

exit 0


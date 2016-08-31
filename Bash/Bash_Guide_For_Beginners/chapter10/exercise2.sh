#!/usr/bin/env bash

# Write a script that implements a simple web browser (in text mode), using wget and links -dump to
# display HTML pages to the user. The user has 3 choices: enter a URL, enter b for back and q to quit.
# The last 10 URLs entered by the user are stored in an array, from which the user can restore the URL
# by using the back functionality.

declare -a bookmarks
bookmarks=(null null null null null null null null null null)
bp=-1 # Bookmark stack pointer.
readonly MAX_BOOKMARKS=10


#==============================================================================
# Functions
#==============================================================================


# Shows the menu of user actions.
show_menu() {
	echo "e) Enter URL."
	echo "b) Go back to previous URL."
	echo "q) Quit."
	read -p ": "
	echo "$REPLY"

}


# Gets a URL from the user.
read_url() {
	echo "Reading URL."

	# url="http://www.google.com/"
	
	read -p "URL: "
	url="$REPLY"

	save_bookmark "$url"
	
	display_web_page "$url"

}


# Saves given bookmark (URL) to bookmark stack.
save_bookmark() {
	url="$1"
	if (( bp < (MAX_BOOKMARKS - 1) )); then
		# Save bookmark to top of stack.
		(( bp++ ))
		bookmarks[$bp]="$url"
	else # Need to shift bookmarks left.
		# Shift bookmarks lef when stack is full.
		(( i = MAX_BOOKMARKS - 1 ));
	    (( i-- ))
		while (( i <= 0 )); do
			(( j = i + 1 ));
			bookmarks[i]=${bookmarks[$j]}
			(( i-- ))
		done

		# Put new bookmark on top of stack.
		(( bp = MAX_BOOKMARKS - 1 ));
		bookmarks[bp]="$url"

	fi

} # save_bookmarks


# Goes back one web page in the bookmark stack.
back() {
	echo "Going back."
	if (( bp == -1 )); then
		return # Bookmark stack is empty, so do nothing.
	else # Bookmark stack not empty.
		url=${bookmarks[$bp]}
		(( bp-- ))
		display_web_page "$url" 
	fi
}


# Displays the given web page.
display_web_page() {
	url="$1"
	echo "Displaying web page for $url."

}


# Quits this program.
quit() {
	echo "Quitting."
	exit 0
}



#==============================================================================
# Main
#==============================================================================

# Reads command from user and executes it.
while (true); do
	clear
	show_menu
	case $REPLY in
		q) quit ;;
		e) read_url ;;
		b) back ;;
		*) : ;;
	esac
	sleep 2

done

	





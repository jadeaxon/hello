#!/usr/bin/env bash

# A 'here document' is like a mini file embedded within a file.

if [ -z "$1" ]; then
	printf "A single non-empty argument is required.\n"
	exit 1
fi

# Double quote expansion:
# <command> <<END_TOKEN
# ...
# END_TOKEN

# Single quote expansion:
# <command> <<'END_TOKEN'
# ...
# END_TOKEN

# Indentation preserving (you can also combine with single quotes):
# <command> <<-END_TOKEN
# \t ...
# END_TOKEN

# By default, here documents undergo same expansion as double quotes.
grep $1 <<EOF
color	green
size	large
weight	heavy
length	long
$1	$1
EOF

# Here's how to single quote the entire here document.
grep $1 <<'OPPOSITE'
this	that
his	hers
if	else
up	down
left	right
$1	$1
OPPOSITE
# WARNING: No extra whitespace or comments can go on the line of the here document end marker.

# You can get proper indentation on a here document using <<-.
# This only works if your intentation is done solely via hard tabs.
# So, this is makes a good case for using hard tabs in source files.
# The fact that makefiles relies on them strengthens the case.
# Also, hard tabs allow people to display whatever tab size they want.
# In addition, they take up less space than soft tabs.
# VERDICT: hard tabs win
if true; then
	echo
	cat <<-'EOF'
		This here document is indented in the bash script.
		But when read, it is not indented.
		You must use hard tabs for the indentation, not spaces.
		Use ':set list' in Vim to check for real tabs (^I).
		So, perhaps Tod was right about using tabs in source files.
	EOF
fi

		

# Assign to a variable? FAIL.
echo "Assigning here document to a variable."
echo
fail_document=<<HERE
this is a here document
assigned to a variable
HERE

# WIN: Use read raw with '' delimiter.
read -r -d '' here_document <<-'EOF'
	abc'asdf"
	$(dont-execute-this)
	foo"bar"''
EOF

echo "$here_document"


# Note that the here document acts as stdin to the command.
# So, you can use it to automate interactive commands that require
# more sophistication than 'yes' but less than 'expect'.




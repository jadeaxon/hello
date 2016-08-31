# Read user input into variable x until x is blank.
# -z seems to consider an all whitespace string empty or else read is autotrimming. 
#
# -z tests for a null string, "".
# read is indeed autotrimming space at beginning and end of line.
while true; do 
	read x 
	echo _${x}_
	[ -z "$x" ] && break 

done 


# If break is given an integer argument, it breaks out of that many levels of loops.
# Implicitly, it breaks out of one level of looping.
# There are not labeled breaks like there are in other (better) languages (like Perl).



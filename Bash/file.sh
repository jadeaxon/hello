#!/usr/bin/env bash

# Get file name from commandline.
file=$1


# Read file line by line.
# Seems to autotrim leading and trailing whitespace, including the newline.
while read line; do 
	echo "read: $line"  
done < "$file"
echo

# If multiple args are supplied to read, then IFS is used to split the line into fields.
# The last arg will get everything remaining on the line, not just a single field.
# So, in the case of 1 arg above, you get the whole line.
while read field0 field1 field2; do
	echo "$field0, $field1, $field2"
done < "$file"
echo

# IFS is the inter-field separator special variable.
# Note how you can prefix a variable assignment to a command and the assignment only applies to that command.
while IFS=i read before_i after_i; do
	echo "${before_i}___${after_i}"
done < "$file"
echo


# Loop over only files that contain spaces in their names.
# Will this pick up files without spaces?  No.
for file in *\ *; do echo "$file"; done


# Simulate grep using a case statement.
# Note that grep is more efficient than bash for regexp handling.
while read line; do 
	case $line in
		# *<regexp>*) ??? 
  		*[Aa].e:*) printf "%s\n" "${line:0:2}" ;; 
  	esac 
done < "$file" 


# Pipe grep into a subshell.
grep query $file | {
	while read line; do
		echo "grepped: $line"
	done

} # grep



exit 0

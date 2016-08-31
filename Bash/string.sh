#!/usr/bin/env bash


# Repeats a given string a given number of times.
# Looks like it actually repeats string until some length is hit.
# USAGE: repeat_string string number 
repeat_string() { 
	result=
	local _string=$1
	local _target_length=$2
  
	# Add repititions until we hit the target length.
	while [ ${#result} -lt $_target_length ]; do 
		result=${result}${_string}
	done 

} 


string="This is a string."
string2='This is also a string.'
string3="interpolated"
string4="You can interpolate inside double quotes. \$string3 = $string3."
string5='You cannot interpolate $string3 inside single quotes.'
string6="Use brackets to disambiguate: ${string}3 vs. $string3."

echo $string
echo $string2
echo $string3
echo $string4
echo $string5
echo $string6
echo

# Appending to a string.
string+="  You can append to a string with the += operator."
echo $string

repeat_string "-" 80
echo $result



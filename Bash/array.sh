# Bash has two kinds of arrays: positional and associative (hashes/dictionaries).

#===============================================================================
# Positional Arrays (integer indexed)
#===============================================================================

# Array indexes are zero-based.
# Arrays can be sparse.

# Test if this version of Bash even supports arrays.
array_test[0]='test' || (echo 'ERROR: Arrays not supported in this version of bash.' && exit 2)

# To (optionally) explicitly declare an array:
declare -a array

# Declare and initialize an array named 'array'.
array=(fee fi fo fum)
array+=(he hay ha ho who) # Add to an array.

# Assign to 5th element of array (indexing is zero-based).
array[4]=mum

# Dereferencing arrays is the weird this.  You must use ${ } to do it.
echo ${array[4]}
echo

# Length of an array.
# Huh, this is reporting the wrong value.  Seems to be length of first element.
echo "Length of array is (not) ${#array}."
echo ${#array}

# Here's how you really do it.
echo "The actual length of the array is ${#array[@]}."

# Length of a string.
string='This is a string.'
echo "Length of strinng is ${#string}."


# Iterate over the array.
for element in "${array[@]}"; do
	echo "$element"
done
echo


# Iterate over a sparse array.
unset array[1] # Remove 'fi'.
for i in "${!array[@]}"; do 
	element=${array[$i]} 
	echo "$element"
done 
echo



# Populate an array with the contents of a file.
# Split on newlines, so each line is a separate array element. 
# Tabs seem to get converted to single spaces in the output.
saved=$IFS
IFS=$'\n'             
array=( $(cat "$0") ) # Slurp this file into an array of lines!
for element in "${array[@]}"; do
	echo "array: $element"
done
echo
IFS=$saved

# If you have bash 4.0+, this is even faster.
# mapfile -t array < "$0"

# Process substitution, pipelines, and mapfile to extract portions of a file. 
mapfile -t comments < <(grep ^# "$0")     
for comment in "${comments[@]}"; do
	echo "comment: $comment"
done
echo

mapfile -t first_words < <(cut -d' ' -f1 "$0" | uniq) # Unique first words.  


#===============================================================================
# Associative Arrays (key => value)
#===============================================================================

# Only available in Bash 4.0+ (?).
# These are like hashes in Perl.

declare -A my_hash

my_hash=( [dog]=mammal [frog]=reptile [turtle]=reptile [fly]=insect ['evil parrot']='die Die DIE!' )
echo ${my_hash[dog]}
echo ${my_hash['evil parrot']}




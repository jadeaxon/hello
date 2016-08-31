#!/usr/bin/env bash

# Alternation generates strings.  Does not match existing filenames (like globbing).
echo {a,b,c}{1,2,3}

# You can use simple ranges.
echo {a..c}{1..3}

# You can have many brace expressions.
echo {0,1}{0,1}{0,1}{0,1}

# A brace expression must contain at least two alternates, else braces treated as 
# literal part of the string.
echo {foo}{bar,baz}

# If you have one alternative, just don't use any braces!
echo foo{bar,baz}


# Alternation happens before variable expansion.
var1=one
var2=two
var3=three
echo $var{1,2,3}

# Alternation happens before globbing.
echo
ls -la hello_{a,b,c}*.sh

# You can loop over generated alternatives.
echo
for i in {0,1}{0,1}{0,1}; do
	echo $i
done



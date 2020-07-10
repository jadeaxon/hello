// No need to declare variable type.
// Variable names start with $.
//
// ""-quoted string literals.
// The . operator for concatenation.
<?php
	$name = "Jeff";
	$i = 3;
	$j = 10;
	echo "$i + $j = " . ($i + $j);
	echo "\n"; // Newline.
	echo "My name is ${name}." // Interpolation in a string literal.
?>


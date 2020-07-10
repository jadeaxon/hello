<?php
	echo "Hello, PHP arrays!\n";
	$guitarists = array(); // Empty array.
	$songs = []; // Also empty array.

	$guitarists = array("Satriani", "EJ", "Santana", "Van Halen"); // Init array.

	// Zero-based index.
	echo $guitarists[0] . "\n";

	// Append to end of array.
	$guitarists[] = "Steve Vai";
	array_push($guitarists, "Wes Montgomery", "Django Reinhardt", "Les Paul"); // Append multiple.

	// FAIL: You cannot use -1 index to access last element.
	// echo $guitarists[-1];

	// Delete array element.
	unset($guitarists[2]);

	// Update element.
	$guitarists[0] = "Satch";
	echo $guitarists[0] . "\n";

	// Split (explode) a string into array elements.
	$values = [];
	$input = "222,13,27,89";
	$values = explode(",", $input); // split
	echo $values[0] . "\n";

	// Join (implode) an array into a string.
	$result = implode(";", $values); // join
	echo $result . "\n";

?>


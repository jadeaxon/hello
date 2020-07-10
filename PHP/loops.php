<?php
	echo "Hello, PHP loops!\n";

	// Basic for loop.
	echo "Count to 10:\n";
	for ($i = 1; $i <= 10; $i++) {
		echo "${i}\n";
	}
	echo "\n";

	// Loop over an array.
	$guitarists = ["Vai", "Satch", "EVH", "EJ", "Hendrix", "Santana"];
	echo "Guitarists:\n";
	for ($i = 0; $i < count($guitarists); $i++) {
		echo $guitarists[$i] . "\n";
	} // next guitarist
	echo "\n";

?>


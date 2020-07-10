<?php
	echo "Hello, PHP loops!\n";

	// Basic for loop.
	echo "Count to 10 (for loop):\n";
	for ($i = 1; $i <= 10; $i++) {
		echo "${i}\n";
	}
	echo "\n";

	// Loop over an array.
	$guitarists = ["Vai", "Satch", "EVH", "EJ", "Hendrix", "Santana"];
	echo "Guitarists (for loop):\n";
	for ($i = 0; $i < count($guitarists); $i++) {
		echo $guitarists[$i] . "\n";
	} // next guitarist
	echo "\n";

	// Basic while loop.
	$i = 0;
	echo "Count to 10 (while loop):\n";
	while ($i < 10) {
		$i++;
		echo "${i}\n";

	} // next iteration
	echo "\n";

	// A do-while loop.
	$i = 0;
	echo "Count to 10 (do-while loop):\n";
	do {
		$i += 1;
		echo "${i}\n";
	}
	while ($i < 10);
	echo "\n";

	// Use a foreach loop to iterate over an array.
	echo "Guitarists (foreach loop):\n";
	foreach ($guitarists as $guitarist) {
		echo "${guitarist}\n";
	} // next guitarist
	echo "\n";

	// Use a foreach loop to iterate over an associative array.
	$item_counts = array(
		"toothpicks" => 37,
		"jelly beans" => 28,
		"dryer sheets" => 19,
		"shirts" => 32
	);

	echo "Item counts (foreach loop):\n";
	foreach ($item_counts as $key => $value) {
		echo "${key} => ${value}\n";
	} // next item count
	echo "\n";

?>


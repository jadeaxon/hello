<?php
	echo "Hello, PHP maps (associative arrays)!\n";
	$jimmy = array(
		"job" => "thief",
		"weapon" => "dagger",
		"nickname" => "The Hand"
	);

	echo $jimmy["nickname"] . "\n";

	// Delete an entry.
	unset($jimmy["weapon"]);

	$item_counts = array(
		"toothpicks" => 37,
		"jelly beans" => 28,
		"dryer sheets" => 19,
		"shirts" => 32
	);

	ksort($item_counts);

	// FAIL: PHP does not pretty print maps automagically.
	// echo $item_counts;

	// Multidimensional arrays.  Nested maps.
	$characters = array(
		"Witch King" => array(
			"HP" => 2,
			"MP" => 100
		),
		"White Knight" => array(
			"HP" => 100,
			"MP" => 2
		)
	);

	echo $characters["Witch King"]["MP"] . "\n";

	// Loop over map with foreach.
	foreach ($item_counts as $key => $value) {
		echo "${key} => ${value}\n";
	} // next item count

?>


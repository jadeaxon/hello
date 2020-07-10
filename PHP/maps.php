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


?>


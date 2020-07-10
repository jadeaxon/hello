<?php
	// Demo various PHP operators.
	echo "left" . " " . "right\n"; // concatenation

	// Basic notes on a guitar.
	$strings = 6;
	$frets = 24;
	$notes = $strings * $frets;
	$notes = $notes + $strings; // Count the open strings.
	echo "There are ${notes} basic notes on a ${strings}-string guitar with ${frets} frets.\n";

?>


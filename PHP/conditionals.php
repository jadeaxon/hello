<?php
	// Demo various PHP operators.
	echo "left" . " " . "right\n"; // concatenation

	// Basic notes on a guitar.
	$strings = 6;
	$frets = 24;
	$notes = $strings * $frets;
	$notes = $notes + $strings; // Count the open strings.
	echo "There are ${notes} basic notes on a ${strings}-string guitar with ${frets} frets.\n";

	if ($notes >= 100) {
		echo "That's a lot of notes!\n";
	}
	else {
		echo "That's a reasonable amount of notes.\n";
	}

	$animal = "cat";
	if ($animal == "cat") {
		echo "Meow!\n";
	}
	else if ($animal == "dog") {
		echo "Woof!\n";
	}
	else if ($animal == "politician") {
		echo "Lies!\n";
	}
	else {
		echo "I don't know what the ${animal} says.";
	}

?>


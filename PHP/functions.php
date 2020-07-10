<?php
	function helloPHP() {
		echo "Hello, PHP functions!\n";
	}

	function hello($name) {
		echo "Hello, ${name}!\n";
	}

	function helloWithDefault($name = "world") {
		hello($name);
	}

	function add($a, $b) {
		return $a + $b;
	}

	helloPHP();
	hello("parameterized functions");
	helloWithDefault();

	$sum = add(13, 22);
	echo "${sum}\n";
?>


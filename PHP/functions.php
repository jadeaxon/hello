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

	helloPHP();
	hello("parameterized functions");
	helloWithDefault();
?>


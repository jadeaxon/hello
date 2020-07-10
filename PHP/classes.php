<?php
	echo "Hello, PHP classes!\n";

	// A class for guitarists.
	class Guitarist {
		public $name;
		public $pickSpeed;
		public $tone;

		// Constructor.
		public function __construct() {
			echo "Guitarist::__construct()\n";
		}
	}

	// An instance of the guitarist class: Joe Satriani.
	$satch = new Guitarist();
	$satch->name = "Joe Satriani";
	$satch->pickSpeed = 88;
	$satch->tone = 80;


?>


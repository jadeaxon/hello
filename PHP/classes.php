<?php
	echo "Hello, PHP classes!\n";

	// A class for guitarists.
	class Guitarist {
		// Public instance variables.
		public $name;
		public $pickSpeed;
		public $tone;

		// Private instance variables.
		private $pickType;

		// Constructor.
		public function __construct() {
			echo "Guitarist::__construct()\n";
			$this->pickType = "unknown";
		}

		// Getter.
		public function getPickType() {
			return $this->pickType;
		}
	}

	// An instance of the guitarist class: Joe Satriani.
	$satch = new Guitarist();
	$satch->name = "Joe Satriani";
	$satch->pickSpeed = 88;
	$satch->tone = 80;

	echo $satch->getPickType() . "\n";

?>


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

	// Base class.
	class Animal {
		public function makeSound() { }
	}

	// Subclass.
	class Toad extends Animal {
		public function makeSound() {
			echo "Ribbit!\n";
		}
	}

	class Fox extends Animal {
		public function makeSound() {
			echo "Yagdaba jag no jag no blam blim blam!\n";
		}

		// Static class function.
		public static function about() {
			echo "This is the fox class.\n";
		}
	}

	// An instance of the guitarist class: Joe Satriani.
	$satch = new Guitarist();
	$satch->name = "Joe Satriani";
	$satch->pickSpeed = 88;
	$satch->tone = 80;

	echo $satch->getPickType() . "\n";

	$toad = new Toad();
	$fox = new Fox();

	$toad->makeSound();
	$fox->makeSound();
	$fox->about();
	$fox::about(); // The more clear way to call a static method.

?>


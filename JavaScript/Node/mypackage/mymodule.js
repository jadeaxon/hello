// This is the main module within the mypackage package.
// You set which module is the main module in package.json.
// By default, the main module is index.js.
// package.json is the metadata file for the package.

// Each module implicitly has a module.exports.
// This is implicitly aliased to exports.
// When you call require() and it finds your module,
// whatever is assigned to module.exports gets returned.

// A normal module function.
var helloWorld = exports.helloWorld = function() {
	console.log("Hello, world!");
};

// A constructor function.  More or less represents a class.
// Contructs a Greeter object.  Call as follows:
// var greeter = new Greeter();
var Greeter = exports.Greeter = function() {
	this.greeting = "Hello, OO JavaScript!";
};

// A method of the Greeter class.
// Greets the caller.
Greeter.prototype.greet = exports.Greeter.prototype.greet = function () {
	console.log(this.greeting);
};

// Constructs an AdvancedGreeter object.
// This is a subclass of Greeter.
var AdvancedGreeter = exports.AdvancedGreeter = function(greetee) {
	Greeter.call(this);
	this.greeting = "Hello, " + greetee;
	this.greetings = 0;
};

// Override the greet() method, but call it in the override.
AdvancedGreeter.prototype.greet = exports.AdvancedGreeter.prototype.greet = function() {
	exports.Greeter.prototype.greet.call(this); // Call the base class method.
	this.greetings++;
}

// Create the inheritance relationship.
var inherits = require("util").inherits;
inherits(AdvancedGreeter, Greeter);




	



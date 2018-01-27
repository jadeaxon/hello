var helloWorld = exports.helloWorld = function() {
	console.log("Hello, world!");
}

// Contructs a Greeter object.  Call as follows:
// var greeter = new Greeter();
var Greeter = exports.Greeter = function() {
	this.greeting = "Hello, OO JavaScript!";
}

// Greets the caller.
exports.Greeter.prototype.greet = function () {
	console.log(this.greeting);
}



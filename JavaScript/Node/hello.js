#!/usr/bin/env node

// To run: node hello.js (just ./hello.js with the shebang).
console.log("Hello, Node.js!");

// Use a local package.
var mymodule = require("./mymodule");
mymodule.helloWorld();

// Use a class from the local packages.
var greeter = new mymodule.Greeter();
greeter.greet();



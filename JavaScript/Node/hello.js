#!/usr/bin/env node

// To run: node hello.js (just ./hello.js with the shebang).
console.log("Hello, Node.js!");

// Use a local package.
var mypackage = require("./mypackage");
mypackage.helloWorld();

// Use a class from the local packages.
var greeter = new mypackage.Greeter();
greeter.greet();



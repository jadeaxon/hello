#!/usr/bin/env node

// To run: node hello.js (just ./hello.js with the shebang).
console.log("Hello, Node.js!");

// Use a local package module.
// Loads the main module from "mypackage" package.
var mymodule = require("./mypackage");
mymodule.helloWorld();

// Use a class from the local packages.
var greeter = new mymodule.Greeter();
greeter.greet();

var AdvancedGreeter = require("./mypackage").AdvancedGreeter;
var advancedGreeter = new AdvancedGreeter("inheritance!");
advancedGreeter.greet();



'use strict';
var assert = require('assert');

var fibModule = require(process.cwd() + '/../fib.js');
var fib = fibModule.fib;
var n, result;

module.exports = function() {

    this.Given(/^I have a (\d+) as n$/, function(number, callback) {
        n = parseInt(number, 10);
        callback();
    });

    this.When(/^I pass n to the fib function$/, function(callback) {
        result = fib(n);
        callback();
    });

    this.Then(/^It calculate the (\d+) as value of the nth term$/, function(value , callback) {
        assert.equal(result, value, 'fib of ' + n +'should be ' + value );
        callback();
    });

};
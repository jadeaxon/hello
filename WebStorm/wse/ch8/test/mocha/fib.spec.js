(function () {
    'use strict';
    var assert = require("assert");

    var fibModule = require('./../../fib.js');
    var fib = fibModule.fib;

    suite('Fibonacci', function () {
        test('Should return the term at the given position', function () {
            assert.equal(fib(0), 0);
            assert.equal(fib(1),1);
            assert.equal(fib(2),1);
            assert.equal(fib(3),2);
            assert.equal(fib(4),3);
            assert.equal(fib(8),21);
            assert.equal(fib(9),34);
            assert.equal(fib(51),20365011074);
        });

        test('Sould return the value as the sum of previous values', function () {
            assert.equal(fib(0) + fib(1), fib(2));
            assert.equal(fib(1) + fib(2), fib(3));
            assert.equal(fib(10) + fib(11), fib(12));
            assert.equal(fib(2500) + fib(2499), fib(2501));
        });
    });

})();

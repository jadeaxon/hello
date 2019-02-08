(function () {
    'use strict';

    var fibModule = require('./../../fib.js');
    var fib = fibModule.fib;

    exports.term = function (test) {
        test.equal(fib(0),0, 'Fibonacci 0 is 0');
        test.equal(fib(1),1, 'Fibonacci 1 is 1');
        test.equal(fib(2),1, 'Fibonacci 2 is 1');
        test.equal(fib(3),2, 'Fibonacci 3 is 2');
        test.equal(fib(4),3, 'Fibonacci 4 is 3');
        test.equal(fib(8),21, 'Fibonacci 8 is 21');
        test.equal(fib(9),34, 'Fibonacci 9 is 34');
        test.equal(fib(51),20365011074, 'Fibonacci 51 is 20365011074');
        test.done();
    };

    exports.recursion = function (test) {
        test.equal(fib(2),fib(0) + fib(1), 'Fibonacci 2 is  fib 0 + fib 1');
        test.equal(fib(3),fib(1) + fib(2), 'Fibonacci 3 is  fib 1 + fib 2');
        test.equal(fib(12),fib(10) + fib(11), 'Fibonacci 12 is  fib 10 + fib 11');
        test.equal(fib(2501),fib(2499) + fib(2500), 'Fibonacci 2501 is  fib 2499 + fib 2500');

        test.done();
    };
})();

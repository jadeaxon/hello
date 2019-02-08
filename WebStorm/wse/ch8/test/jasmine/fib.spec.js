(function () {
    'use strict';

    var fib = window.fib;

    describe('Fibonacci', function () {

        it('Should return the term at the given position', function () {
            expect(fib(0)).toEqual(0);
            expect(fib(1)).toEqual(1);
            expect(fib(2)).toEqual(1);
            expect(fib(3)).toEqual(1);
            expect(fib(4)).toEqual(3);
            expect(fib(8)).toEqual(21);
            expect(fib(9)).toEqual(34);
            expect(fib(51)).toEqual(20365011074);
        });

        it('Sould return the value as the sum of previous values', function(){
            expect(fib(0) + fib(1)).toEqual(fib(2));
            expect(fib(1) + fib(2)).toEqual(fib(3));
            expect(fib(10) + fib(11)).toEqual(fib(12));
            expect(fib(2500) + fib(2499)).toEqual(fib(2501));
        });

    });
})();

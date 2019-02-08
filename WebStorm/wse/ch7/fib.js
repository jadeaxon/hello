/**
 * Utility functions.
 */
var util = function () {
    /**
     * Memoize a function, i.e. given a function f, create a new function g
     * that when applied will call f, and cache values returned from f. The
     * arguments to f are used as the cache key.
     * @param {function} f The function to memoize.
     * @returns {function} The memoized function.
     */
    var memoize = function memoize(f) {

        var cache = {};

        return function () {

            var args = Array.prototype.slice.apply(arguments);
            var key = JSON.stringify(args);

            if (!cache.hasOwnProperty(key)) {
                cache[key] = f.apply(this, args);
            }

            return cache[key];
        };
    };


    /**
     * Determine whether a variable is an integer.
     * @param {mixed} n The variable to test.
     * @returns {boolean}
     */
    var isInteger = function (n) {

        return (
            Object.prototype.toString.call(n) === '[object Number]' &&
            n % 1 === 0 &&
            isNaN(n) === false
        );
    };

    return {
        memoize: memoize,
        isInteger: isInteger
    };
}();

/**
 * Compute the nth term in the Fibonacci series:
 * 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
 * @param {integer} n Index into the series.
 * @returns {integer} The nth term.
 * @throws {Error} If an invalid argument is passed.
 */
var fib = function (n) {
    if (!util.isInteger(n) || n < 0) {
        throw new Error('Invalid argument: ' + n);
    }
    return (n < 2) ? n : fib(n - 1) + fib(n - 2);
};

// Replace fib with a memoized version
fib = util.memoize(fib);



for (var i = 1; i < 100; i++) {
    var isNode = false;

    // Export the Underscore object for **CommonJS**, with backwards-compatibility
    // for the old `require()` API. If we're not in CommonJS, add `_` to the
    // global object.
    if (typeof module !== 'undefined' && module.exports) {
        isNode = true;
    }

    if (isNode){
        console.log(fib(i))
    }else{
        var div = document.createElement('div');
        div.textContent = 'i: ' + i + ' - fib :' + fib(i);
        document.body.appendChild(div);
    }
}
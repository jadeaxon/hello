/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const langs = ['JavaScript', 'Ruby', 'Python', 'Clojure'];
{
  const firstElement = langs[0];
  const lastElement = langs[langs.length - 1]; //eh?
}

console.log(langs.first);
console.log(langs.last);

Object.defineProperties(Array.prototype, {
  first: {
    get: function() { return this[0]; },
    set: function(value) { this[0] = value; }
  },
  last: {
    get: function() { return this[this.length - 1]; },
    set: function(value) { this[Math.max(this.length - 1, 0)] = value; }
  }  
});

const firstElement = langs.first;
const lastElement = langs.last;

console.log(firstElement);
console.log(lastElement);

langs.first = 'Modern JavaScript';
langs.last = 'ClojureScript';

console.log(langs);


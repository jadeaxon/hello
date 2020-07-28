/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const a = 4;
const c = undefined;

console.log(a == null);
console.log(c == null);

console.log(a === null);
console.log(c === null);

console.log(a === undefined);
console.log(c === undefined);

console.log(c === null || c === undefined);

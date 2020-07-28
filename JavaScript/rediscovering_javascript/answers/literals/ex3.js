/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const beforeAndAfter = function(number) {
  if(number < 0) return [];
  if(number === 0) return [1];

  return [number - 1, number + 1];
};

let before = 0;
let after = 0;
               
//Your code goes before =
[before, after] = beforeAndAfter(7);
console.log(`${before} and ${after}`); //6 and 8

[before, after] = beforeAndAfter(9);
console.log(`${before} and ${after}`); //8 and 10

[before, after = 0] = beforeAndAfter(0);
console.log(`${before} and ${after}`); //0 and 1

[before = 0, after = 0] = beforeAndAfter(-1);
console.log(`${before} and ${after}`); //0 and 0

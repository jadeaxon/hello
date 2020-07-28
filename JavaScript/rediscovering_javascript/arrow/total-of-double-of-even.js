/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const numbers = [1, 5, 2, 6, 8, 3, 4, 9, 7, 6];

let totalOfDoubleOfEven = 0;
                               
for(const number of numbers) {
  if(number % 2 === 0) {
    totalOfDoubleOfEven += number * 2;
  }
}

console.log(totalOfDoubleOfEven);
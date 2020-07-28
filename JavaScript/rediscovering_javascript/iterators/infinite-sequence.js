/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const isPrime = function(number) {
  for(let i = 2; i < number; i++) {
    if(number % i === 0) return false;
  }
  
  return number > 1;
};

const primesStartingFrom = function*(start) {
  let index = start;
  
  while(true) {
    if(isPrime(index)) yield index;
    index++;
  }
};
            
for(const number of primesStartingFrom(10)) {
  process.stdout.write(number + ', ');
  if(number > 25) break;
}

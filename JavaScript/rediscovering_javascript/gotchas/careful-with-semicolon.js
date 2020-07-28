/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
//BROKEN CODE
const compute = function(number) {
  if(number > 5) {
    return number 
      + 2; 
  }

  if(number > 2) {
    return
      number * 2;
  } 
};

console.log(compute(6));
console.log(compute(3));
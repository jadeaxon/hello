/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
const sample = function(number) {
  factor = 4;
  
  if(number == 2) {
    return 
      number * factor;
  }
  
  return number * 10;
};
          
console.log(sample(2));
/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const max = function() {
  console.log(arguments instanceof Array);
    
  let large = arguments[0];
    
  for(let i = 0; i < arguments.length; i++) {
    if(arguments[i] > large) {
      large = arguments[i];
    }
  }
    
  return large;
};
  
console.log(max(2, 1, 7, 4));

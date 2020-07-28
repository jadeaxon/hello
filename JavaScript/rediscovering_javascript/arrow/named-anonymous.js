/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

{
  setTimeout(function repeat(count) {
    console.log('called...');             
    if(count > 1)
      setTimeout(repeat.bind(null, count - 1), 1000);
  }.bind(null, 5), 1000);  
}            
{            
  const repeat = function repeat(count) {
    console.log('called...');             
    if(count > 1)
      setTimeout(repeat.bind(null, count - 1), 1000);
  };
  
  setTimeout(repeat.bind(null, 5), 1000);  
}

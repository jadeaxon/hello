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
  const create = function(message) {
    console.log('First argument for create: ' + arguments[0]); 
    return function() { 
      console.log('First argument seen by greet: ' + arguments[0]);  
    };
  };

  const greet = create('some value');
  greet('hi');
}

{
  const create = function(message) {
    console.log('First argument for create: ' + arguments[0]);
    return () => console.log('First argument seen by greet: ' + arguments[0]);  
  };

  const greet = create('some value');
  greet('hi');
}

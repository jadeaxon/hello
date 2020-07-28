/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const greet = function(msg, name) { 
  const pleasantry = typeof(this) === 'string' ? this : 'have a nice day';
  console.log(`${msg} ${name}, ${pleasantry}`);
};

greet('Howdy', 'Jane');
greet.call('how are you?', 'Howdy', 'Jane');
greet.apply('how are you?', ['Howdy', 'Jane']);

Reflect.apply(greet, 'how are you?', ['Howdy', 'Jane']);

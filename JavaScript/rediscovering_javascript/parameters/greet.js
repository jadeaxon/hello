/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
  
const greet = function(...names) {
  console.log('hello ' + names.join(', '));
};

const jack = 'Jack';
const jill = 'Jill';
greet(jack, jill);
             

const tj = ['Tom', 'Jerry'];  
greet(tj[0], tj[1]);

greet(...tj);

greet.apply(null, tj); //no more stinky null

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const addAge = function(person, theAge) {
  return {first: person.first, last: person.last, age: theAge };
};

const parker = { first: 'Peter', last: 'Parker', 
  email: 'spiderman@superheroes.example.com' };

console.log(addAge(parker, 15));

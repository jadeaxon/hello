/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const createPerson = function(name, age, sport, sportFn) {
  return {
    name,
    age,
    toString() {
      return `${this.name} ${this.age}`;
    },
    [`play${sport}`] : sportFn
  };
};

const sam = 
  createPerson('Sam', 21, 'Soccer', 
    function() { console.log(`${this.name}, kick, don't touch`); });
    
console.log(sam.name);
console.log(sam.toString());
sam.playSoccer();

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const Movie = class Show {
  constructor() {
    console.log('creating instance...');
    console.log(Show);
  }
};

console.log('Movie is the class name');
console.log(Movie);
const classic = new Movie('Gone with the Wind');

try {             
  console.log('however...');      
  console.log(Show);
} catch(ex) {
  console.log(ex.message);
}

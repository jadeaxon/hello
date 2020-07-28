/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const text = new String('live');

try {
  text.reverse();
} catch(ex) {
  console.log(ex.message);
}

text.reverse = function() { return this.split('').reverse().join(''); };

console.log(text.reverse());

const anotherText = new String('rats');

try {
  console.log(anotherText.reverse());  
} catch(ex) {
  console.log(ex.message);
}


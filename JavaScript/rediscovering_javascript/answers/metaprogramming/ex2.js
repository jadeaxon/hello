/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

Number.prototype.percent = function() {
  if(this >= 1) {
    throw new Error('value should be less than 1');
  }
  
  return `${this * 100}%`;
};

const value1 = 0.35;
const value2 = 0.91;

console.log(value1.percent()); //35%
console.log(value2.percent()); //91%

try {                        
  const value3 = 44;
  console.log(value3.percent());
} catch(ex) {
  console.log(ex.message); // value should be less than 1
}
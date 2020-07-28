/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

Set.prototype.combine = function(otherSet) {
  const copyOfSet = new Set(this);
  
  for(const element of otherSet) {
    copyOfSet.add(element);
  }
  
  return copyOfSet;
};

const names1 = new Set(['Tom', 'Sara', 'Brad', 'Kim']);
const names2 = new Set(['Mike', 'Kate']);

const combinedNames = names1.combine(names2);

console.log(names1.size);
console.log(names2.size);
console.log(combinedNames.size);
console.log(combinedNames);

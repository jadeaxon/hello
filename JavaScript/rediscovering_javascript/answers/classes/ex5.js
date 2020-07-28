/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const create = function(sports) {
  return new Set(sports.map(sport => sport.toUpperCase()));
};

const toLowerCase = function(sports) {
  return new Set([...sports].map(sport => sport.toLowerCase()));
};

const sports = create(['Soccer', 'Football', 'Cricket', 'Tennis', 'soccer']);

console.log(sports.has('FOOTBALL')); //true
console.log(sports.has('Football')); //false
console.log(sports.size); //4

const inLowerCase = toLowerCase(sports);
console.log(inLowerCase.has('football'));
console.log(inLowerCase.size); //4

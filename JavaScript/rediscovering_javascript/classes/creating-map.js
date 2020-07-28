/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const scores = 
  new Map([['Sara', 12], ['Bob', 11], ['Jill', 15], ['Bruce', 14]]);

scores.set('Jake', 14);

console.log(scores.size);

for(const [name, score] of scores.entries()) {
  console.log(`${name} : ${score}`);
}

scores.forEach((score, name) => console.log(`${name} : ${score}`));

scores.forEach(score => console.log(score));

console.log(scores.has('Jane'));
console.log(scores.has('Jill'));
     
const another = new Map();
another.set(1, 2);
console.log(another);

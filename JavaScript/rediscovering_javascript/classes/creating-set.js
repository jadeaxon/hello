/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const names = new Set(['Jack', 'Jill', 'Jake', 'Jack', 'Sara']);
  
console.log(names.size);

names.add('Mike');

names.add('Kate')
  .add('Kara');

console.log(names.has('Brad'));                                         

console.log(names.entries());
console.log(names.keys());
console.log(names.values());

for(const name of names) {
  console.log(name);
}

names.forEach(name => console.log(name));

[...names].filter(name => name.startsWith('J'))
  .map(name => name.toUpperCase())
  .forEach(name => console.log(name));

const another = new Set();
console.log(
  another.add('a')
    .add(1));

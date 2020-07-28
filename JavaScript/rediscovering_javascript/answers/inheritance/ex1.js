/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class FunctionalSet extends Set {
  filter(predicate) {
    return new FunctionalSet([...this].filter(predicate));
  }

  map(mapper) {
    return new FunctionalSet([...this].map(mapper));
  }

  reduce(accumulator, identity) {
    return [...this].reduce(accumulator, identity);
  }
}

const set = new FunctionalSet(['Jack', 'Jill', 'Tom', 'Jerry']);

const jSet = set.filter(name => name.startsWith('J'));
const allCaps = set.map(name => name.toUpperCase());

const totalLengthOfJWords =
  set.filter(name => name.startsWith('J'))
    .reduce((total, word) => total + word.length, 0);

console.log(jSet); //FunctionalSet { 'Jack', 'Jill', 'Jerry' }
console.log(allCaps); //FunctionalSet { 'JACK', 'JILL', 'TOM', 'JERRY' }
console.log(totalLengthOfJWords); //13

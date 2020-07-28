/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class BoundedSet extends Set {
  constructor(capacity, initialValues) {
    super();
    this.capacity = capacity;

    if(initialValues.length <= capacity) {
      initialValues.forEach(value => this.add(value));
    }
  }

  add(value) {
    if(this.has(value)) return;

    if(this.size < this.capacity) {
      super.add(value);
    } else {
      throw new Error(`exceeded capacity of ${this.capacity} elements`);
    }
  }
}

const set = new BoundedSet(5, ['Apple', 'Banana', 'Grape', 'Mangoe']);

set.add('Orange');
set.add('Apple');

try {
  set.add('Tangerine');
} catch(ex) {
  console.log(ex.message); //exceeded capacity of 5 elements
}

set.delete('Grape');
set.add('Peach');
console.log(set.size); //5

const set2 = new BoundedSet(2, ['Apple', 'Banana', 'Grape']);
console.log(set2.size); //0
console.log(set2); //BoundedSet { capacity: 2 }

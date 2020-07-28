/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Person {
  constructor(age) {
    this.age = age;
  }                
  
  play() { console.log(`The ${this.age} year old is playing`); }
  
  get years() { return this.age; }
}

const sam = new Person(2);

console.log(sam.age);
sam.play();

const fieldName = 'age';
const methodName = 'play';

console.log(sam[fieldName]);
sam[methodName]();

console.log(`Members of sam: ${Object.keys(sam)}`);

for(const property in sam) {
  console.log(`Property: ${property} value: ${sam[property]}`);
}

console.log(Object.getOwnPropertyNames(Reflect.getPrototypeOf(sam)));

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Counter {
  constructor() {
    this.count = 0;
  }                
  
  incrementBy(value) { this.count += value; return this.count; }
  decrementBy(value) { this.count -= value; return this.count; }
}

const call = function(counter, method, ...data) {
  const methodToCall = Reflect.get(counter, method);
  return Reflect.apply(methodToCall, counter, data);
};

const counter = new Counter();

console.log(call(counter, 'incrementBy', 10)); //10
console.log(call(counter, 'decrementBy', 7)); //3
console.log(counter.count); //3
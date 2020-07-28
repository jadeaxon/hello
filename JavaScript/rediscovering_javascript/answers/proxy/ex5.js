/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
          
const proxy = new Proxy(Set.prototype, {
  get: function(target, propertyName, receiver) {
    return receiver.has(propertyName);
  }
});

Reflect.setPrototypeOf(Set.prototype, proxy);
                                           
const fruits = new Set(['Apple', 'Banana', 'Orange', 'Jack Fruit']);
                         
console.log(fruits.size);           //4
console.log(fruits.Apple);          //true
console.log(fruits.Banana);         //true
console.log(fruits.Orange);         //true
console.log(fruits['Jack Fruit']);  //true
console.log(fruits.Tomato);         //false
/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Base {
  copy() {            
    const constructor = 
      Reflect.getPrototypeOf(this).constructor[Symbol.species] ||
        Reflect.getPrototypeOf(this).constructor;
        
    return new constructor();
  }
}

class Derived1 extends Base {
  static get [Symbol.species]() {
    return Base;
  }
}

class Derived2 extends Base {
  static get [Symbol.species]() {
    return Derived2;
  }
}
                                               
const derived1 = new Derived1();
const derived2 = new Derived2();

console.log(derived1.copy()); //Base {}
console.log(derived2.copy()); //Derived2 {}

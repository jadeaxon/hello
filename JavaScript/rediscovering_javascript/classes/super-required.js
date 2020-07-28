/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Base {}

class Derived1 extends Base {
  constructor() {
    console.log('Derived1');
    super();
    this.something = 4;
  }
}

class Derived2 extends Base {
  constructor() {
    console.log('Derived2');
    this.something = 4;
  }
}

class Derived3 extends Base {
  constructor() {
    console.log('Derived3');
    this.something = 4; 
    super();
  }
}

class Derived4 extends Base {
}

new Derived1();

try {
  new Derived2();
}catch(ex) {
  console.log(ex.message);
}

try {
  new Derived3();
}catch(ex) {
  console.log(ex.message);
}

new Derived4();
console.log('done');

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const counterFactory = function() {
  class Counter {
    constructor() { this.value = 0; }
    increment() { this.value += 1; }
    
    get count() { return this.value; }
  }

  const { proxy: counterProxy, revoke: revokeFunction } = 
    Proxy.revocable(new Counter(), {});
  
  const leaseTime = 100;
  setTimeout(revokeFunction, leaseTime);
  
  return counterProxy;
};

const counter = counterFactory();

const incrementAndDisplay = function() {
  try {
    counter.increment();
    console.log(counter.count);
    setTimeout(incrementAndDisplay, 20);
  } catch(ex) {
    console.log(ex.message);
  }
};

incrementAndDisplay();

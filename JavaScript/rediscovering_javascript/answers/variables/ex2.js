/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

function first() {
  for(let i = 0; i < 5; i++) {
    second();
  }
}

function second() {
  for(let i = 0; i < 3; i++) {
    console.log(i);
  }
}

first();

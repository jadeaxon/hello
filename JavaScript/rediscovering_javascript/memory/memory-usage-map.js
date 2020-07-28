/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
(function() {
"use strict";

const MAX = 100000000;
const map = new Map();

for(let i = 0; i <= MAX; i++) {
  const key = {index: i};
  map.set(key, i);
}

console.log("DONE");
})();
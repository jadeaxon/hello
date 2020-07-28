/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
class CardDeck {
  constructor() {
    this.suitShapes = ['Clubs', 'Diamonds', 'Hearts', 'Spaces'];
  }
  
  *[Symbol.iterator]() {
    yield this.suitShapes[0];
    yield this.suitShapes[1];
    yield this.suitShapes[2];
    yield this.suitShapes[3];
  }
}

const deck = new CardDeck();

for(const suit of deck) {
  console.log(suit);
}

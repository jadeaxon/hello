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

  *suits() {
    for(const color of this.suitShapes) {
      yield color;
    }
  }

  *pips() {
    yield 'Ace';
    yield 'King';
    yield 'Queen';
    yield 'Jack';
    
    for(let i = 10; i > 1; i--) {
      yield i.toString();
    }
  }

  *suitsAndPips() {
    yield* this.suits();
    yield* this.pips();
  }
}

const deck = new CardDeck();

for(const suit of deck.suits()) {
  console.log(suit);
}

for(const pip of deck.pips()) {
  process.stdout.write(pip + ', ');
}
console.log();

for(const value of deck.suitsAndPips()) {
  process.stdout.write(value + ' ');
}
console.log();

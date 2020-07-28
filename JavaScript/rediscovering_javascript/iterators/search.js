/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
class SuperHero {
  constructor(name, realName) {
    this.name = name;
    this.realName = realName;
  }
                               
  toString() { return this.name; }
  
  [Symbol.search](value) {  
    console.info('this: ' + this + ', value: ' + value);
    return value.search(this.realName);
  }
}

const superHeroes = [
  new SuperHero('Superman', 'Clark Kent'),
  new SuperHero('Batman', 'Bruce Wayne'),
  new SuperHero('Ironman', 'Tony Stark'),
  new SuperHero('Spiderman', 'Peter Parker') ];

const names = 'Peter Parker, Clark Kent, Bruce Wayne';
for(const superHero of superHeroes) {
  console.log(`Result of search: ${names.search(superHero)}`);
}

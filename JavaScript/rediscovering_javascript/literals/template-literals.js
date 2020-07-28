/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const name1 = 'Jack';
const name2 = 'Jill';

console.log('Hello ' + name1 + ' and ' + name2);

console.log(`Hello ${name1} and ${name2}`);

console.log(`Hello ${name1} and $name2`);

const item = 'cake';
console.log(`The kid asked, "how's the ${item}?"`);

const price = 1;
console.log(`The price of a { symbol is $${price * 0.01 }.`);

console.log(`Shout out greetings: ${'hello'.toUpperCase()}`);

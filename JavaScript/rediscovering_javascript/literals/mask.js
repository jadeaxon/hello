/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const mask = function(texts, ...expressions) {

  const createMask = (text) => '*'.repeat(text.length);

  const maskedText = expressions
    .map((expression, index) =>
      `${texts[index]}${createMask(expression.toString())}`)
    .join('');

  const closingText = texts[texts.length - 1];

  return `${maskedText}${closingText}`;
};

const agent = 'Bond';
const organization = 'MI6';

console.log(mask`Hi, I'm ${agent}, with ${organization}.`);

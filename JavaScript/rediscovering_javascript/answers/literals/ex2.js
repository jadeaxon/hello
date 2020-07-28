/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const stripMargin = function(texts, ...expressions) {             
  const exceptLast = expressions.map(function(expression, index) {
    return `${texts[index]}${expression.toString().toUpperCase()}`;
  }).join('');
  
  const result = `${exceptLast}${texts[texts.length - 1]}`;
  
  return result.replace(/[\n][\t\s]+(\w)/g, ' $1').trim();
};

const name = 'Jane';

const processed = stripMargin` This is for
  ${name} and it needs to be
	delivered by December 24th.`;

  
console.log(processed);
//This is for JANE and it needs to be delivered by December 24th.

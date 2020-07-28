/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const success = function(value) {
  return { value: value };
};

const blowup = function(value) {
  throw new Error('blowing up with value ' + value);
};

const process = function(successFn, errorFn) {
  const value = Math.round(Math.random() * 100, 2);
  
  if(value > 50) {
    return successFn(value);
  } else {
    return errorFn(value);
  }
};

try {
  console.log(process(success, blowup));  
} catch(ex) {
  console.log(ex.message);
}

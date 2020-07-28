/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const compute = async function(number) {
  if(number < 0) {
    return Promise.reject('no negative, please');
  }
  return Promise.resolve(number * 2);
};

//can still use then and catch on async functions
const callCompute = function(number) {
  compute(number)
    .then(result => console.log(`Result is ${result}`))
    .catch(error => console.log(error));
}

callCompute(2);
callCompute(-1);
/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const computeSqrtAsync = function(number) {
  if(number < 0) {
    return Promise.reject('no negative number, please.');
  }
  
  if(number === 0) {
    return Promise.resolve(0);
  }
  
  return new Promise(function(resolve, reject) {
    setTimeout(() => resolve(Math.sqrt(number)), 1000);
  });
};

const forNegative1 = computeSqrtAsync(-1);
const forZero = computeSqrtAsync(0);
const forSixteen = computeSqrtAsync(16);

console.log(forNegative1);
console.log(forZero);
console.log(forSixteen);

const reportOnPromise = function(promise) {
  promise
    .then(result => console.log(`result is ${result}.`))
    .catch(error => console.log(`ERROR: ${error}`));
};

reportOnPromise(forNegative1);
reportOnPromise(forZero);
reportOnPromise(forSixteen);

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const createPromise = function(timeInMillis) {
  return new Promise(function(resolve, reject) {
    setTimeout(() => resolve(timeInMillis), timeInMillis);
  });
};

const createTimeout = function(timeInMillis) {
  return new Promise(function(resolve, reject) {
    setTimeout(() => reject(`timeout after ${timeInMillis} MS`), timeInMillis);
  });
};

Promise.race([createPromise(1000), createPromise(2000), createTimeout(3000)])
  .then(result => console.log(`completed after ${result} MS`))
  .catch(error => console.log(`ERROR: ${error}`));

Promise.race([createPromise(3500), createPromise(4000), createTimeout(2000)])
  .then(result => console.log(`completed after ${result} MS`))
  .catch(error => console.log(`ERROR: ${error}`));

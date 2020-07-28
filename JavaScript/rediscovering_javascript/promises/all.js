/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const fs = require('fs-extra');
const request = require('request-promise');

const countPrimes = function(number) {
  if(isNaN(number)) {
    return Promise.reject(`'${number}' is not a number`);
  }
  
  return request(`http://localhost:8084?number=${number}`)
    .then(count => `Number of primes from 1 to ${number} is ${count}`);
};

const countPrimesForEachLine = function(pathToFile) {
  fs.readFile(pathToFile)
    .then(content => content.toString())
    .then(content =>content.split('\n'))
    .then(lines => Promise.all(lines.map(countPrimes)))
    .then(counts => console.log(counts))
    .catch(error => console.log(error));    
};

countPrimesForEachLine('numbers.txt');
countPrimesForEachLine('numbers-with-error.txt');

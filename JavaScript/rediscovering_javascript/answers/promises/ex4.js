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

const createTimeout = function(timeInMillis) {
  return new Promise(function(resolve, reject) {
    setTimeout(() => reject(`timeout ${timeInMillis} MS`), timeInMillis);
  });
};

const logAndTerminate = function(err) {
  console.log(err);
  process.exit(1);
};                  

const countPrimesForEachLine = function(pathToFile) {
  fs.readFile(pathToFile)
    .then(content => content.toString())
    .then(content =>content.split('\n'))
    .then(lines => Promise.race(
        [Promise.all(lines.map(countPrimes)), createTimeout(1000)]))
    .then(counts => console.log(counts))
    .catch(logAndTerminate);    
};

countPrimesForEachLine('numbers.txt');
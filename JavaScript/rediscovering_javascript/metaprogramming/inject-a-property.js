/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const today = new Date();

Object.defineProperty(today, 'isInLeapYear', {
  get: function() {
    const year = this.getFullYear();
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }
});               

console.log(`${today.getFullYear()} is a leap year?: ${today.isInLeapYear}`);

Object.defineProperty(Date.prototype, 'isInLeapYear', {
  get: function() {
    const year = this.getFullYear();
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }
});               

for(const year of [2018, 2019, 2020, 2021]) {
  const yayOrNay = new Date(year, 1, 1).isInLeapYear ? '' : 'not ';
  console.log(`${year} is ${yayOrNay}a leap year`);
}

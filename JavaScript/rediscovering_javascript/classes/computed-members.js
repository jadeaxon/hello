/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const NYD = `New Year's Day`;

class Holidays {
  constructor() {
    this[NYD] = 'January 1';
    this["Valentine's Day"] = 'February 14';
  }
  
  ['list holidays']() {
    return Object.keys(this);
  }
}

const usHolidays = new Holidays();
usHolidays['4th of July'] = 'July 4';

console.log(usHolidays[`Valentine's Day`]);         
const methodName = 'list holidays';
console.log(usHolidays[methodName]());

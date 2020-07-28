/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const getDetails = function(
  {name, born: { year: birthYear }, graduated: {year}}) {
  return `${name} born in the year ${birthYear}, graduated in ${year}.`;
};

const details =
  getDetails({name: 'Sara',
    born: { month: 1, day: 1, year: 2000 },
    graduated: { month: 5, day: 31, year: 2018 }});

console.log(details);
//Sara born in the year 2000, graduated in 2018.

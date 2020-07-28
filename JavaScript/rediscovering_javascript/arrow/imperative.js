/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const pickNamesInUpperCaseOfLength = function(names, length) {
  let result = '';

  for(let i = 0; i < names.length; i++) {
    if(names[i].length === length) {
      result += names[i].toUpperCase() + ', ';
    }
  }

  return result.substring(0, result.length - 2);                      
};

const names = ['Paul', 'Sara', 'Bruce', 'Darla', 'Brad', 
  'Nancy', 'Mike', 'Susan'];

console.log(pickNamesInUpperCaseOfLength(names, 5));

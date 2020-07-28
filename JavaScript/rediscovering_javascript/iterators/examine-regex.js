/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const regex = /cool/;
            
process.stdout.write('regex is of type RegExp: ');
console.log(regex instanceof RegExp);
        
process.stdout.write('Properties of regex: ');
console.log(Object.getOwnPropertyNames(regex));
                                                           
process.stdout.write('Symbol properties of regex: ');                                                           
console.log(Object.getOwnPropertySymbols(regex));          

console.log("Symbol properties of regex's prototype: ");                                                           
console.log(Object.getOwnPropertySymbols(Object.getPrototypeOf(regex)));

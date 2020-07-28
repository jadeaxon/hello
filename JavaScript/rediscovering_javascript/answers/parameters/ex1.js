/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const amountAfterTaxes = function(amount, ...taxes) {
  const computeTaxForAmount = function(tax) {
    return amount * tax / 100.0;
  };
  
  const totalValues = function(total, value) { 
    return total + value; 
  };              
  
  return taxes.map(computeTaxForAmount)
    .reduce(totalValues, amount).toFixed(2);

  //or, using arrow functions:
  //return taxes.map(tax => amount * tax / 100.0)
  //  .reduce((total, value) => total + value, amount)
  //  .toFixed(2);
};

const amount = 25.12;              
const fedTax = 10;                    
const stateTax = 2;
const localTax = 0.5;

console.log(amountAfterTaxes(amount)); //25.12
console.log(amountAfterTaxes(amount, fedTax)); //27.63
console.log(amountAfterTaxes(amount, fedTax, stateTax)); //28.13
console.log(
  amountAfterTaxes(amount, fedTax, stateTax, localTax)); //28.26
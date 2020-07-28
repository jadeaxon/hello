/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const placeOrder = function(
  id, amount, 
  shipping = (amount < 20 ? 5 : 10), 
  date = new Date()) {
  console.log(' shipping charge:$' + shipping + ' Date:' + date.getDate());
};
                         
placeOrder(1, 12.10, undefined, new Date('05/15/2018'));

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const hours = 14;
const event = 'meeting';
                                                               
const when = (hrs) => 
  hrs < 12 ? 'in the morning' : 
    `later in the day, in the ${hrs < 20 ? 'evening' : 'night'}`;

console.log(`The ${event} will happen ${when(hours)}.`);

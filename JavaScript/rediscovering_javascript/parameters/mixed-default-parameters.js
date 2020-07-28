/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const badFetchData = function(
  location = { host: 'localhost', port: 443 }, 
  id, 
  uri = 'employees') {
    
  console.log('Fetch data from https://' + 
    location.host + ':' + location.port + '/' + uri);
};  

badFetchData(undefined, 4, 'magazines');

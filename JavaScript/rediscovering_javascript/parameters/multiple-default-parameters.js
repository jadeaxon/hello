/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
const fetchData = function(
  id, 
  location = { host: 'localhost', port: 443 }, 
  uri = 'employees') {
    
  console.log('Fetch data from https://' + 
    location.host + ':' + location.port + '/' + uri);
};

fetchData(1, { host: 'agiledeveloper', port: 404 }, 'books');
fetchData(1, { host: 'agiledeveloper', port: 404 });
fetchData(2);

fetchData(3, undefined, 'books');

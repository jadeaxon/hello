/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
var isPerfect = function(number) {
  var sumOfFactors = 0;

  for(index = 1; index <= number; index++) {
    if(number % index == 0) {
      sumOfFactors += index;
    }
  }

  return sumOfFactors 
    == number * 2;
}; 

for(i = 1; i <= 10; i++) {
  console.log('is ' + i + ' perfect?: ' + isPerfect(i));
}
/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
const letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

for(const [i, letter] of letters.entries()) {
  if(i % 3 === 0)
    console.log(letter);
}
/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
class Message {
  constructor(text) { this.text = text; }
  
  [Symbol.replace](word, substitute) {
    return this.text.replace(word, substitute);
  }
}

const message = new Message('There are no stupid questions.');

console.log('stupid'.replace(message, 's*****'));
//There are no s***** questions.

console.log(''.replace(message, 'Yes, '));
//Yes, There are no stupid questions.
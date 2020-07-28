/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Book {
  constructor(title, author, pages) {
    this.title = title;
    this.author = author;
    this.numberOfPages = pages;
    this.sales = 0;
  }                            
  
  get pages() { return this.numberOfPages; }
  
  get copiesSold() { return this.sales; }
  set copiesSold(value) {
    if(value < 0) throw new Error(`Value can't be negative`);
    
    this.sales = value;
  }
}

const book = new Book('Who Moved My Cheese?', 'Spencer Johnson', 96);
console.log(book.title); //Who Moved My Cheese
console.log(book.pages); //96

try {
  book.pages = 96;
} catch(ex) {
  console.log(ex.message);
  //Cannot set property pages of #<Book> which has only a getter
}

console.log(book.copiesSold); //0
book.copiesSold = 1;
console.log(book.copiesSold); //1

try {
  book.copiesSold = -2;
} catch(ex) {
  console.log(ex.message);//Value can't be negative
}
console.log(book.copiesSold); //1
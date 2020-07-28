/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Todo {
  constructor() {
    this['learn JavaScript'] = 'done';
    this['write elegant code'] = 'work-in-progress';
    this['automate tests'] = 'work-in-progress';
  }
  
  get completedCount() {
    return Object.keys(this)
      .filter(key => this[key] === 'done')
      .length;
  }
}

const todo = new Todo();
console.log(todo['learn JavaScript']); //'done'
console.log(todo['write elegant code']);//'work-in-progress'
console.log(todo['automate tests']);//'work-in-progress'
console.log(todo.completedCount); //1
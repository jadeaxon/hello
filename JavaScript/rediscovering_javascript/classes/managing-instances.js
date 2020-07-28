/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Names {
  constructor(...names) {
    this.names = names;
  }

  filter1(selector) {
    return new Names(...this.names.filter(selector));
  }

  filter2(selector) {
    const constructor = Reflect.getPrototypeOf(this).constructor;
    
    return new constructor(...this.names.filter(selector));
  }

  filter3(selector) {
    const constructor = 
      Reflect.getPrototypeOf(this).constructor.kindHint ||
        Reflect.getPrototypeOf(this).constructor;
    
    return new constructor(...this.names.filter(selector));
  }
}


class SpecializedNames extends Names {
  static get kindHint() {
    return Names;
  }
}

const specializedNames = new SpecializedNames('Java', 'C#', 'JavaScript');

console.log(specializedNames.filter1(name => name.startsWith('Java')));

console.log(specializedNames.filter2(name => name.startsWith('Java')));

console.log(specializedNames.filter3(name => name.startsWith('Java')));

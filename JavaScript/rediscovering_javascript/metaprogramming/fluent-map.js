/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const langsAndAuthors = new Map([
  ['JavaScript', 'Eich'], ['Java', 'Gosling']]);

const accessLangsMap = function(map) {
  console.log(`Number of languages: ${map.size}`);
  console.log(`Author of JavaScript: ${map.get('JavaScript')}`);
  console.log(`Asking fluently: ${map.JavaScript}`);
};

accessLangsMap(langsAndAuthors);

const handler = {
  get: function(target, propertyName, receiver) {
    if(Reflect.has(target, propertyName)) {
      const property = Reflect.get(target, propertyName);

      if(property instanceof Function) { //existing method, bind and return
        return property.bind(target);
      }                            

      //existing property, return as-is
      return property;
    }

    //synthesize property: we assume it is a key
    return target.get(propertyName);
  }
};

const proxy = new Proxy(langsAndAuthors, handler);

accessLangsMap(proxy);

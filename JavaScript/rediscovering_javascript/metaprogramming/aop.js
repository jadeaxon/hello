/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const greet = function(message, name) {
  return `${message} ${name}!`;
};

const invokeGreet = function(func, name) {
  console.log(func('hi', name));
};

invokeGreet(greet, 'Bob');

const beforeAdvice = new Proxy(greet, {
  apply: function(target, thisArg, args) {
    const message = args[0];
    const msgInCaps = message[0].toUpperCase() + message.slice(1);
    
    return Reflect.apply(target, thisArg, [msgInCaps, ...args.slice(1)]);
  }
});         

invokeGreet(beforeAdvice, 'Bob');

const beforeAndAfterAdvice = new Proxy(greet, {
  apply: function(target, thisArg, args) {                       
    const newArguments = ['Howdy', ...args.slice(1)];
    
    const result = Reflect.apply(target, thisArg, newArguments);
    
    return result.toUpperCase();
  }
});         

invokeGreet(beforeAndAfterAdvice, 'Bob');

const aroundAdvice = new Proxy(greet, {
  apply: function(target, thisArg, args) {
    if(args[1] === 'Doc') {
      return "What's up, Doc?";      
    }
    else {
      return Reflect.apply(target, thisArg, args);      
    }
  }
});         

invokeGreet(aroundAdvice, 'Bob');
invokeGreet(aroundAdvice, 'Doc');

/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
                                           
const createPlayMethodProxy = function(instance) {
  const handler = {
    get: function(target, propertyName) {
      if(propertyName.startsWith('play')) {
        const activity = propertyName.substring(4);

        if(target.activities.includes(activity)) {
          return () => `I love to play ${activity}`;
        } else {
          return () => `I don't play ${activity}`;
        }
      } else {
        throw new Error(`${propertyName} is not a function`);
      }
    }
  };
  
  return new Proxy(instance, handler);
};
                                                                          
const proxy = createPlayMethodProxy({ activities: ['Football', 'Tennis'] });

console.log(proxy.playTennis());   //I love to play Tennis
console.log(proxy.playFootball()); //I love to play Football
console.log(proxy.playPolitics()); //I don't play Politics

try {
  console.log(proxy.dance());
} catch(ex) {
  console.log(ex.message); //dance is not a function
}
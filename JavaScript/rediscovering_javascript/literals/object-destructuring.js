/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const weight = 'WeightKG';

const sam = {
  name: 'Sam',
  age: 2,
  height: 110,
  address: { street: '404 Missing St.'},
  shipping: { street: '500 NoName St.'},
  [weight]: 15,
  [Symbol.for('favoriteColor')]: 'Orange',
};

{
  const firstName = sam.name;
  const theAge = sam.age;
  console.log(`${firstName} ${theAge}`);
}

{
  const { name: firstName, age: theAge } = sam;
  console.log(`${firstName} ${theAge}`);
}

{
  const { name: firstName, age: theAge } = { name: 'Sam', age: 2, height: 110 };
  console.log(`${firstName} ${theAge}`);
}

{
  const { name, age: theAge } = sam;
  console.log(`${name} ${theAge}`);
}

{
  const { [weight]: wt, [Symbol.for('favoriteColor')]: favColor } = sam;
  console.log(`${wt} ${favColor}`);
}

{
  const { lat, lon, favorite = true} = {lat: 84.45, lon: -114.12};
  console.log(`${lat} ${lon} ${favorite}`);
}

{
  const printInfo = function(person) {
    console.log(`${person.name} is ${person.age} years old`);
  };                                                        

  printInfo(sam);
}

{
  const printInfo = function({name: theName, age: theAge}) {
    console.log(`${theName} is ${theAge} years old`);
  };                                                        
  
  printInfo(sam);
}

{
  const printInfo = function({name, age}) {
    console.log(`${name} is ${age} years old`);
  };                                                        
  
  printInfo(sam);
}

{
  const { name, address: { street } } = sam;
  
  console.log(street);
  
  try {
    console.log(address);
  } catch(ex) {
    console.log(ex.message);
  }
}

{
  const { name, address: { street }, shipping: { street: shipStreet } } = sam;
  
  console.log(`${street} ${shipStreet}`);
}

{
  let theName = '--';
  ({ name: theName } = sam);

  console.log(theName);
}

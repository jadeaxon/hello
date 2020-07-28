/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

class Employee {
  constructor(firstName, lastName, yearOfBirth) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.yearOfBirth = yearOfBirth;
  }                

  get fullname() { return `${this.firstName} ${this.lastName}`; }
  get age() { return new Date().getFullYear() - this.yearOfBirth; }
}                                                          

const printInfo = function(employee) {
  console.log(`First name: ${employee.firstName}`);
  console.log(`Fullname: ${employee.fullname}`);
  console.log(`Age: ${employee.age}`);
};

const john = new Employee('John', 'Doe', 2010);

{
  const handler = {};
  const proxyDoe = new Proxy(john, handler);
  printInfo(proxyDoe);
}

{
  const handler = {
    get: function(target, propertyName, receiver) {
      if(propertyName === 'firstName') {
        console.log(`target is john? ${john === target}`);
        console.log(`propertyName is ${propertyName}`);
        console.log(`receiver is proxyDoe? ${proxyDoe === receiver}`);      
      }
    
      return Reflect.get(target, propertyName);
    }
  };
  const proxyDoe = new Proxy(john, handler);
  printInfo(proxyDoe);
}

{
  const handler = {
    get: function(target, propertyName, receiver) {
      if(propertyName === 'age') {
        return `It's not polite to ask that question, dear`;
      }
    
      return Reflect.get(target, propertyName);
    }
  };
  const proxyDoe = new Proxy(john, handler);
  printInfo(proxyDoe);
}

"use strict";

import { ToString } from './decorators.mjs';

@ToString({exclude: ['age']})
export default class Person {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;         
    this.age = age;
  }
}                                                 

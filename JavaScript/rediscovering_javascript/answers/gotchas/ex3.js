/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';

const canVote = function(age) {
  if(age === 18) {
    return 'yay, start voting';
  }

  if(age > 17) {
    return "please vote";
  }

  return "no, can't vote";
};

console.log(canVote(12));      //no, can't vote
console.log(canVote("12"));    //no, can't vote
console.log(canVote(17));      //no, can't vote
console.log(canVote('@18'));   //no, can't vote
console.log(canVote(18));      //yay, start voting
console.log(canVote(28));      //please vote

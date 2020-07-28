/***
 * Excerpted from "Rediscovering JavaScript",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material,
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose.
 * Visit http://www.pragmaticprogrammer.com/titles/ves6 for more book information.
***/
'use strict';
  
const fs = require('fs');

const displayFileContent = function(pathToFile) {
  const handleFile = function(err, contents) {
    if(err) {
      console.log(err.message);
    } else {
      console.log(contents.toString());
    }
  };

  try {
    fs.readFile(pathToFile, handleFile);    
  } catch(ex) {
    console.log(ex.message);
  }
};

displayFileContent('readfile.js');

displayFileContent('does-not-exits');

displayFileContent();

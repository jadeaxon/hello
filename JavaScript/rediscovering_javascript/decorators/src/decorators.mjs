"use strict";
export const ToString = function(properties) {

  const exclude = (properties && properties.exclude) || [];
	
  return function(target) {
    target.prototype.toString = function() {
      return Object.keys(this)
        .filter(key => !exclude.includes(key))
        .map(key => `${key}: ${this[key]}`)
        .join(', ');
    };

    return target;
  }
}

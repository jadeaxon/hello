"use strict";

import 'reflect-metadata';

export const Component = function(properties) {
  return function(target) {         
    Reflect.defineMetadata('annotations', properties, target);
    return target;
  };
}

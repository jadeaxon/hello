module.exports = function (wallaby) {
  return {
    files: ['fib.js'],
    tests: ['test/jasmine/*.spec.js']
  };
};
exports.config = {
  // This is where Selenium Server is running.
  seleniumAddress: 'http://localhost:4444/wd/hub',
  // This is your test file.  The tests will run in Chrome by default.
  specs: ['test.spec.js']
};
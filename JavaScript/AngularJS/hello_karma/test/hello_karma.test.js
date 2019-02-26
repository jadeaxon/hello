// Protractor tests.
// PRE: npm install -g protractor
// PRE: webdriver-manager update
// PRE: webdriver-manager start
// PRE: Create protractor.conf.js
// protractor protractor.conf.js

// FAIL: The app doesn't load in the remote-controlled browser.
describe('End-to-end app tests', function () {
  beforeEach(function () {
    browser.get('http://localhost:63342/hello_karma/site/index.html');
  });

  it('ng-repeat', function () {
    var list = element.all(by.repeater('city in cities'));
    expect(list.count()).toEqual(5);
  });
});


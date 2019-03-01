// Protractor tests.
// PRE: npm install -g protractor
// PRE: webdriver-manager update
// PRE: webdriver-manager start
// PRE: Create protractor.conf.js
// PRE: Follow these instructions to make a Protractor run/debug config: https://www.jetbrains.com/help/webstorm/protractor.html.
// PRE: Configure this in WebStorm: "Allow unsigned requests" option enabled (Settings | Build, Execution, Deployment | Debugger).

describe('End-to-end app tests', function () {
  beforeEach(function () {
    browser.get('http://localhost:63342/hello_karma/site/index.html');
  });

  it('ng-repeat', function () {
    var list = element.all(by.repeater('city in cities'));
    expect(list.count()).toEqual(5);
  });
});


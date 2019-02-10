The point of this app is to get basic Karma/Jasmine unit testing working from WebStorm.

# Initialize your project to use NPM packages.
# This will create packages.json.
npm init

# Install Karma.
# --save-dev saves the NPM package as a development dependency (not a runtime dependency).
# That is, Karma is used as part of your development environment, not part of the app you are building.
npm install karma --save-dev

# Install Karma plugin to use Jasmine tests.
# Jasmine is a unit test framework.  Karma is a test runner that supports multiple unit test frameworks.
npm install karma-jasmine --save-dev

# Install Karma plugin that lets it launch Chrome.
npm install karma-chrome-launcher --save-dev

# Make it easy to call Karma.
npm install -g karma-cli

# Generate a Karma config file: karma.conf.js.
# Use test/**/*Spec.js to look for test files.
# Karma calls them "test specifications".
karma init

# Run your tests, assuming you have defined any.
# There's actually little test run icons that appear in the editor gutter.  That's how I'm starting the tests.
# This pops up a "Test Run" tab at the bottom left in WebStorm.  Expand all test results to see a specific test.
# This is the test runner tab of the run tool window.  There's also a Karma Server tab.
karma start

# To run all tests in WebStorm, see
https://www.jetbrains.com/help/webstorm/running-unit-tests-on-karma.html
Actually, right click on a single .spec.js test file and run it.
Now, edit that run configuration that WebStorm created.  There's a radio button to run all tests.
Rename your run configuration to "Unit Tests" or whatever.
<A-S r> -- rerun the last set of tests that were run

You have to use angular-mocks.js.
Your karma.conf.js files section has to point to this and all JavaScript libs and custom code in your project.
Finally, it has to point at the JavaScript tests.
This causes all the code to be loaded into the browser it is running the tests in.



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
karma start

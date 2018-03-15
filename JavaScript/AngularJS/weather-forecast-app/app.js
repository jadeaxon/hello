// Run this using live-server.

// Module
// The main point of this is to provide an overall scope for everything in our AngularJS app.
// The other point is to include all the other modules our app module depends on.
// You need to use <html ng-app="weatherApp"> to make index.html be governed by this AngularJS
// module.  The combination of this JavaScript module and all .html files becomes the whole app.
var weatherApp = angular.module('weatherApp', ['ngRoute', 'ngResource']);

// Models -- just a single variable wrapped by a service
// Views -- pages/*.html
// View Models -- $scope injected into controllers
// Controllers -- controllers.js
// Services -- services.js
// Routes -- routes.js
// Directives -- directives.js and directives/*.html


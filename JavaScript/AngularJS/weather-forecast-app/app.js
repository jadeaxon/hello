// Run this using live-server.

// Module
var weatherApp = angular.module('weatherApp', ['ngRoute', 'ngResource']);

// Controllers
// Uses the minification-friendly version of DI.
weatherApp.controller('homeController', ['$scope', function ($scope) {

}]);


weatherApp.controller('forecastController', ['$scope', function ($scope) {

}]);

// Routes
// All the subpages are brought over during the initial HTTP request with the single AngularJS page
// (thus SPA).  These subpage request are routed locally on the browser.  They don't involve the web
// server.
// PRE: You need an element tagged with ng-view in your main HTML page to route to these subpages.
// PRE: Include ngRoute in app module deps.
weatherApp.config(function ($routeProvider) {
	$routeProvider
		// http://127.0.0.1:8080/index.html#/
		.when('/', {
			templateUrl: 'pages/home.html',
			controller: 'homeController'
		})
		// http://127.0.0.1:8080/index.html#/forecast
		.when('/forecast', {
			templateUrl: 'pages/forecast.html',
			controller: 'forecastController'
		})
	;

});



// Run this using live-server.

// Module
// The main point of this is to provide an overall scope for everything in our AngularJS app.
// The other point is to include all the other modules our app module depends on.
// You need to use <html ng-app="weatherApp"> to make index.html be governed by this AngularJS
// module.  The combination of this JavaScript module and all .html files becomes the whole app.
var weatherApp = angular.module('weatherApp', ['ngRoute', 'ngResource']);

// Services
// This will provide data shared between the scopes of the different subpages (views).
// This service gets injected into our controllers.
// Whenever you hit the browser refresh button, the service reinitializes its state.
// Simply navigating to different app subpages (#/foo URLs) should preserve state since that's all
// client-side navigation/routing.
//
// Our services collectively provide an API for accessing our overall system model.  Each service
// might help us access a particular class of objects, like cities.
// These client-side services might then call server-side services to read/write to a database so
// we get session, account, and system persistence.
//
// Daily forecast URL: http://api.openweathermap.org/data/2.5/forecast/daily?APPID=d48a9c26f43f66550ea09daea8feae43
weatherApp.service('cityService', function () {
	this.city = "Provo, UT";

});

// Views
// These are in the pages/ subdir.

// Controllers
// Uses the minification-friendly version of DI.
// We inject $scope into our controller.  Each controller gets its own scope.  This is the view model.
// We also inject our service into the controllers.
weatherApp.controller('homeController', ['$scope', 'cityService', function ($scope, cityService) {
	// Get the initial city value from the service.
	$scope.city = cityService.city;

	// Whenever $scope.city changes, update the value in the service.
	$scope.$watch('city', function () {
		cityService.city = $scope.city;
	});

}]);


weatherApp.controller('forecastController', ['$scope', 'cityService', function ($scope, cityService) {
	// Get the initial city value from the service.
	$scope.city = cityService.city;

	// Whenever $scope.city changes, update the value in the service.
	$scope.$watch('city', function () {
		cityService.city = $scope.city;
	});

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



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
		// http://127.0.0.1:8080/index.html#/weather
		.when('/weather', {
			templateUrl: 'pages/weather.html',
			controller: 'weatherController'
		})
		// http://127.0.0.1:8080/index.html#/weather/<attribute>
		// This parses part of the URL into $routeParams.attribute.
		// Notice the : before attribute.
		// We'll inject $routeParams into our controller to get the value into scope.
		.when('/weather/:temp_type', {
			templateUrl: 'pages/weather.html',
			controller: 'weatherController'
		})
	;

});


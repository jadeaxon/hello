// Controllers
// Uses the minification-friendly version of DI.
// We inject $scope into our controller.  Each controller gets its own scope.  This is the view model.
// We also inject our service into the controllers.
// The $window service lets us control the browser window.
weatherApp.controller('homeController', ['$scope', '$location', 'cityService', function ($scope, $location, cityService) {
	// Get the initial city value from the service.
	$scope.city = cityService.city;

	// Whenever $scope.city changes, update the value in the service.
	$scope.$watch('city', function () {
		cityService.city = $scope.city;
	});

	// Make the query submit on hitting enter in the input field.
	// No longer use this since we've converted the previous mechanism to an actual form.
	/*
	$scope.submitOnEnter = function (keyEvent) {
		if (keyEvent.which === 13) {
			// alert("The Enter key was pressed.");
			// cityService.city = $scope.city; // This gets set if we click the button, but not if we leave page from here.
			// $scope.$apply(function () { }); /// Does not help.  See below.
			// alert(document.getElementById("city").value); // Does this update as user types?  Yes.
			// The problem is, this call has the same as a refresh.  Entire new request, so all
			// controller state is lost.  How do we just do a client-side redirect?
			// $window.open("#/weather");
			// Goddam AngularJS now wants a ! after the #: // https://stackoverflow.com/questions/41211875/angularjs-1-6-0-latest-now-routes-not-working.
			// Nope, we're using 1.3 from back in 2014 in this app since that's when the Udemy course was recorded.
			// $location.path("#/weather"); // Goddam AngularJS bullshit API: // https://stackoverflow.com/questions/20201860/why-is-angular-replacing-my-hashtag-into-23.
			// FUCKING FUCK!!!  API version hell plus bad documentation plus dynamic language plus OS/browser versions plus character encodings plus request, session, and
			// five billion other scopes plus client and server MV* pattern plus Daylight Fucking Savings Time!  I should have been a brain surgeon with rocket science as
			// a side hobby to relax--much easier.  Fuck.
			var path = $location.path() + "weather"; // This is bullshit.
			$location.path(path);
			$location.replace();
		}
	};
	*/

	// Submit the weather forcast request/query/form.
	$scope.submit = function () {
		$location.path("/weather");
	};
}]);


weatherApp.controller(
	'weatherController',
	['$scope', '$resource', '$routeParams', 'cityService', function ($scope, $resource, $routeParams, cityService) {
		// Get the initial city value from the service.
		$scope.city = cityService.city;
		var temp_type = $routeParams.temp_type || 'current_temp';
		$scope.temp_type = temp_type;

		// There's a slight bit of voodoo happening here.
		$scope.weatherAPI = $resource(
			'http://api.openweathermap.org/data/2.5/weather',
			{ callback: 'JSON_CALLBACK' },
			{ get: { method: 'JSONP' } }
		);

		// Once we define this resource getter, we can use it to get the resource.
		// Pass in request params as a JavaScript object.
		$scope.weatherResult = $scope.weatherAPI.get({
			q: $scope.city + ',us', // Provo,us
			units: 'imperial', // For Farenheit temps.
			APPID: 'd48a9c26f43f66550ea09daea8feae43'
		});

		// console.log(attribute);
		// console.log(result);

		/* This blows up the page.
		$scope.temperature = '???';
		if (temp_type === 'current_temp') {
			$scope.temperature = $scope.weatherResult.main.temp;
		}
		else if (temp_type === 'min_temp') {
			$scope.temperature = $scope.weatherResult.main.temp_min;
		}
		else if (temp_type === 'max_temp') {
			$scope.temperature = $scope.weatherResult.main.temp_max;
		}

		// It can log $scope.weatherResult clearly showing it has a main attribute.
		// But when you try to access it, it blows up as being undefined.
		var result = $scope.weatherResult;
		console.log($scope.weatherResult.main);
		console.log($scope.weatherResult);
		console.log($scope.weatherResult.main.temp);

		*/

		// Whenever $scope.city changes, update the value in the service.
		$scope.$watch('city', function () {
			cityService.city = $scope.city;
		});
	}]
);


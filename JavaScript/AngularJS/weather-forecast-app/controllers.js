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


// theApp is a global var we created in main.js.
// Note sure what this function-def-inside () syntax is about.
(function(app){
	'use strict';

	app.controller("appController", function($scope) {
		$scope.title = "Welcome to Angular Material";
		$scope.message = "This message will appear under the title.";
	});

})(theApp);


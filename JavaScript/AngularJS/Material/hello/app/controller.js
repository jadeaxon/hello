// theApp is a global var we created in main.js.
// Note sure what this function-def-inside () syntax is about.
// All it does is invoke the function in its own scope.

/*
(function(app){
	'use strict';

	app.controller("appController", function($scope) {
		$scope.title = "Welcome to Angular Material";
		$scope.message = "This message will appear under the title.";
	});

})(theApp);
*/

// Wrapping the code in the function again seems like needless complexity.
'use strict';
theApp.controller("appController", function($scope) {
	$scope.title = "Welcome to Angular Material";
	// We can shove this in the HTML template using {{<expression>}} syntax.
	$scope.message = "This message will appear under the title.";
});



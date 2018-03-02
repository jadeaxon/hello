// All this accomplishes is calling the function in its own scope.
/*
var theApp = (function (angularRef) {
	'use strict';
	return angularRef.module('helloAngularMaterialApp', ['ngMaterial']);
})(angular);
*/

// Yes, it looks like it was just needless complexity.
'use strict';
var theApp = angular.module('helloAngularMaterialApp', ['ngMaterial']);



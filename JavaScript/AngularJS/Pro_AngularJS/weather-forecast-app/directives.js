// Directives
// Custom directives let you make your own HTML tags and attributes.
// The camel case directive name gets converted to <temperature-navbar> for the tag.
weatherApp.directive("temperatureNavbar", function () {
	var directive = {};
	directive.restrict = 'E';
	directive.templateUrl = 'directives/temperatureNavbar.html';
	directive.scope = {
		myLabel: '@'
	};
	return directive;
});



var directives = angular.module("directives", []);

// Define a custom attribute directive.
// If we apply jsa-title to any element, it will replace it with the HTML template.
// jsaTitle => jsa-title in the HTML.
directives.directive("jsaTitle", function () {
  return {
    // Note that the directive has access to its parent element's scope.
    // You can also access attributes of the controller, not just its scope.
    controller: "MainCtrl",
    controllerAs: "ctrl", // The this.* of the controller, not $scope.
    // Note how you can {{}} interpolate inside an HTML attribute value.
    template: "<h2 id='{{ctrl.ctrlid}}'>Chapter {{chapter}}: {{topic}}</h2>"
  };
});

// Another custom directive.  This one uses transclusion.
directives.directive("jsaPane", function () {
  return {
    // Wherever you use ng-transclude in the template, the original contents of the element you are
    // replacing will be inserted there.
    transclude: true,
    templateUrl: 'directives/jsaPane.html',

    // This makes it so the title attribute is visible in the element created by our custom directive.
    scope: {title: '@'}
  };
});
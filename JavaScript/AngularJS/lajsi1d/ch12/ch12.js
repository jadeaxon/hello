var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.chapter = 12;
  $scope.topic = "Custom Directives";
  $scope.message = "This is chapter " + $scope.chapter + ".";

  // A controller attribute.
  this.ctrlid = 'jsa-title1';
});

// Define a custom attribute directive.
// If we apply jsa-title to any element, it will replace it with the HTML template.
// jsaTitle => jsa-title in the HTML.
app.directive("jsaTitle", function () {
  return {
    // Note that the directive has access to its parent element's scope.
    // You can also access attributes of the controller, not just its scope.
    controller: "MainCtrl",
    controllerAs: "ctrl", // The this.* of the controller, not $scope.
    // Note how you can {{}} interpolate inside an HTML attribute value.
    template: "<h2 id='{{ctrl.ctrlid}}'>Chapter {{chapter}}: {{topic}}</h2>"
  };
});
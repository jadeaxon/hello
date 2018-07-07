// This file stores all the AngularJS directives for the app.
var module = angular.module("customDirectives", []);
module.directive("customMultiButton", function () {
  return {
    scope: { counter: "=counter" },
    link: function (scope, element, attrs) {
      element.on("click", function (event) {
        console.log("Button click: " + event.target.innerText);
        scope.$apply(function () {
          scope.counter++;
        });
      });
    }
  }
});


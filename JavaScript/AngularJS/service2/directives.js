// This file stores all the AngularJS directives for the app.
var app = angular.module("exampleApp");
app.directive("triButton", function () {
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


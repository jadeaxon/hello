// This file stores all the AngularJS directives for the app.
var module = angular.module("customDirectives", []);
module.directive("customMultiButton", function ($$log, $$debug, $$error, $$plog) {
  return {
    scope: { counter: "=counter" },
    link: function (scope, element, attrs) {
      element.on("click", function (event) {
        $$log.log("Button click: " + event.target.innerText);
        $$debug.log("Button clicked.");
        $$error.log("Button clicked.");
        $$plog.log("The button was clicked.");
        scope.$apply(function () {
          scope.counter++;
        });
      });
    }
  }
});


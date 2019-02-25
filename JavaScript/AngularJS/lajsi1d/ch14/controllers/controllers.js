// Since window.controllers is an existing thing, we need to put this in a different scope.
// We can do this via an immediately invoked function.
(function () {
  var controllers = angular.module("controllers", []);

  controllers.controller("ModuleCtrl", function ($scope) {
    $scope.chapter = 14;
    $scope.topic = "Events";
    $scope.message = "This is chapter " + $scope.chapter + ".";
  });

})();

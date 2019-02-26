var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "Chapter 20: ng-include";
  $scope.submitted = false;

  $scope.processForm = function () {
    $scope.submitted = true;
  };
});


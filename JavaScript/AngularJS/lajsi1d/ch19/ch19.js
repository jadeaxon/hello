var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "Chapter 19: Form Submission";
  $scope.submitted = false;

  $scope.processForm = function () {
    $scope.submitted = true;
  };
});


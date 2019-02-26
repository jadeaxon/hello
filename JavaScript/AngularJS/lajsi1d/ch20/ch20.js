var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "Chapter 20: ng-include";
  $scope.submitted = false;

  $scope.includeFiles = true;

  $scope.processForm = function () {
    $scope.submitted = true;
  };
});

// Load external content into a div.
$(function () {
  // It places it inside the <div>; it does not replace the <div>.
  $('div#content').load('content.html');
});


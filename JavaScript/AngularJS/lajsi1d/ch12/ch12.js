var app = angular.module("app", ["directives"]);

app.controller("MainCtrl", function ($scope) {
  $scope.chapter = 12;
  $scope.topic = "Custom Directives";
  $scope.message = "This is chapter " + $scope.chapter + ".";

  // Number of times a <jsa-click-counter> has been clicked.
  $scope.clicks = 0;

  // A controller attribute.
  this.ctrlid = 'jsa-title1';
});

// This file holds all the controllers for the app.

var app = angular.module("customControllers", []);
app.controller("defaultCtrl", function ($scope, $$log) {
  $scope.data = {
    cities: ["London", "New York", "Paris", "Tokyo"],
    totalClicks: 0
  };
  $scope.$watch('data.totalClicks', function (newVal) {
    $$log.log("Total click count: " + newVal);
  });
});


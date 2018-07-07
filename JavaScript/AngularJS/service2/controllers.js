// This file holds all the controllers for the app.

var app = angular.module("exampleApp");
app.controller("defaultCtrl", function ($scope) {
  $scope.data = {
    cities: ["London", "New York", "Paris"],
    totalClicks: 0
  };
  $scope.$watch('data.totalClicks', function (newVal) {
    console.log("Total click count: " + newVal);
  });
});


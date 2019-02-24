var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "This is chapter 11."

  $scope.holidays = [
    'Thanksgiving',
    'Easter',
    'Christmas',
    "Valentine's Day",
    'Labor Day',
    'Spring Break',
    'Memorial Day',
    'Independence Day',
    'Pioneer Day'
  ]

});

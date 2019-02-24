var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "This is chapter 8."

  $scope.person = {
    name: "Frodo Baggins",
    height: "3'4\"",
    home: "The Shire",
    money: 1234567890.0987654321
  };

});

var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "This is chapter 6."

  $scope.person = {
    firstName: null,
    lastName: null
  };

  $scope.people = [];

  $scope.addPerson = function () {
    console.log('Pushed the Add Person button.');
    // Clone the existing person object and push the clone onto our list of people.
    // $scope.people.push(JSON.parse(JSON.stringify($scope.person)));
    $scope.people.push($scope.person);
    $scope.person = { firstName: null, lastName: null }; // Make a new person.
    console.log($scope.people)
  };
});

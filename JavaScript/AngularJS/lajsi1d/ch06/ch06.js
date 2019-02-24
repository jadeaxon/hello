var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "This is chapter 6."

  $scope.person = {
    firstName: null,
    lastName: null,
    description: null,
    os: null // Preferred OS.
  };

  $scope.people = [];

  // These are used as options of the preferred OS <select>.
  $scope.oses = {
    mac: "Mac",
    nix: "Linux",
    win: "Windows",
    dos: "FreeDOS"
  };

  // Adds a person to the list of people.
  // Linked to Add Person button via ng-click.
  $scope.addPerson = function () {
    console.log('Pushed the Add Person button.');
    // Clone the existing person object and push the clone onto our list of people.
    // $scope.people.push(JSON.parse(JSON.stringify($scope.person)));
    $scope.people.push($scope.person);
    $scope.person = { firstName: null, lastName: null, description: null }; // Make a new person.
    console.log($scope.people)
  };
});

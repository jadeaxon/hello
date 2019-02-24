// Include the ngRoute module as a dependency.
var app = angular.module("app", ['ngRoute']);

app.config(function ($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'views/start.html',
    controller: 'StartCtrl'
  });
  $routeProvider.when('/bedroom', {
    templateUrl: 'views/bedroom.html',
    controller: 'BedroomCtrl'
  });
  $routeProvider.when('/hallway', {
    templateUrl: 'views/hallway.html',
    controller: 'HallwayCtrl'
  });
  $routeProvider.otherwise({
    templateUrl: 'views/error.html',
    controller: 'ErrorCtrl'
  });
});

app.controller("MainCtrl", function ($scope) {
  $scope.gameTitle = "Rooms of Doom"

});

app.controller("StartCtrl", function ($scope, $location) {
  $scope.startGame = function () {
    $location.path('/bedroom');
  };
});

app.controller("BedroomCtrl", function ($scope, $location) {
  $scope.name = "Bedroom";
  $scope.description = "You are in a bedroom.  To the east is a hallway.";
  $scope.goEast = function () {
    $location.path('/hallway');
  };
});

app.controller("HallwayCtrl", function ($scope, $location) {
  $scope.name = "Hallway";
  $scope.description ="You are in a hallway.  To the west is a bedroom.";
  $scope.goWest = function () {
    $location.path('/bedroom');
  };
});

app.controller("ErrorCtrl", function ($scope) {
  $scope.errorMessage = "You navigated to an invalid app URL.";
});
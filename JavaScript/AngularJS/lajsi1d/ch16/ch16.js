// Include the ngRoute module as a dependency.
var app = angular.module("app", ['ngRoute']);

app.config(function ($routeProvider, $locationProvider) {
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

  // Put : in front of an identifier to extract to that variable within the scope.
  $routeProvider.when('/object/:type/:id', {
    templateUrl: 'views/object.html',
    controller: 'ObjectCtrl'
  });
  $routeProvider.otherwise({
    templateUrl: 'views/error.html',
    controller: 'ErrorCtrl'
  });
});

app.controller("MainCtrl", function ($scope) {
  $scope.gameTitle = "Rooms of Doom"

});

// Inject $routeParams to access parameters extracted from the URL.
app.controller("ObjectCtrl", function ($scope, $routeParams) {
  $scope.type = $routeParams.type;
  $scope.id = $routeParams.id;
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

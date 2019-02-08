'use strict';

// This is a non-app module in which we define our custom controllers.
// The only difference between the controllers is the message data stored in their scope.

var helloWorldControllers = angular.module('helloWorldControllers', []);

helloWorldControllers.controller('MainCtrl', ['$scope', '$location', '$http',
    function MainCtrl($scope, $location, $http) {
        $scope.message = "Hello, AngularJS! (MainCtrl)";
    }]);

helloWorldControllers.controller('ShowCtrl', ['$scope', '$location', '$http',
    function ShowCtrl($scope, $location, $http) {
        $scope.message = "Hello, AngularJS (ShowCtrl)";
    }]);
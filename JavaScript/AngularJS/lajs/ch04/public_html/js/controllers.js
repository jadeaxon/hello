'use strict';

(function() {

// This module contains all the controllers for our app.
var controllers = angular.module('helloWorld.controllers', []);

// The common convention is for controller names to end with Ctrl.
controllers.controller('MainCtrl', ['$scope',
    function MainCtrl($scope) {
        $scope.message = "Hello, world!";
    }]);

controllers.controller('ShowCtrl', ['$scope',
    function ShowCtrl($scope) {
        $scope.message = "Show the world about controllers.";
    }]);

controllers.controller('CustomerCtrl', ['$scope',
    // Initialize the scope.
    // Variables and functions defined in the scope are available in the view template this controller is attached to.
    // No need to name the function passed here.
    function CustomerCtrl($scope) {
        $scope.customerName = "MgRonald's";
        $scope.customerNumber = 666;
        $scope.changeCustomer = function () {
            $scope.customerName = $scope.cName;
            $scope.customerNumber = $scope.cNumber;
        };
    }]);

controllers.controller('AddCustomerCtrl', ['$scope', '$location',
    function AddCustomerCtrl($scope, $location) {
        $scope.submit = function () {
            $location.path('/addedCustomer/' + $scope.cName + "/" + $scope.cCity);
        };
    }]);

controllers.controller('AddedCustomerCtrl', ['$scope', '$routeParams',
    function AddedCustomerCtrl($scope, $routeParams) {
        $scope.customerName = $routeParams.customer;
        $scope.customerCity = $routeParams.city;
    }]);

})();
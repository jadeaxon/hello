'use strict';

(function () {

// This module contains all the controllers for our app.
var controllers = angular.module('helloWorld.controllers', []);

// The common convention is for controller names to end with Ctrl.
controllers.controller('MainCtrl', ['$scope',
    function ($scope) {
        $scope.message = "Hello, world!";
    }]);

controllers.controller('ShowCtrl', ['$scope',
    function ($scope) {
        $scope.message = "Show the world about controllers.";
    }]);

controllers.controller('CustomerCtrl', ['$scope',
    // Initialize the scope.
    // Variables and functions defined in the scope are available in the view template this controller is attached to.
    // No need to name the function passed here.
    function ($scope) {
        $scope.customerName = "MgRonald's";
        $scope.customerNumber = 666;
        $scope.changeCustomer = function () {
            $scope.customerName = $scope.cName;
            $scope.customerNumber = $scope.cNumber;
        };
    }]);

controllers.controller('AddCustomerCtrl', ['$scope', '$location',
    function ($scope, $location) {
        // This is bound to HTML form via ng-submit.
        // cName and cCity are bound to HTML input elements.
        $scope.submit = function () {
            // Move to a new URL.
            // This does not cause an HTTP request since we're going to a URL routed to this SPA.
            $location.path('/addedCustomer/' + $scope.cName + "/" + $scope.cCity);
        };
    }]);

controllers.controller('AddedCustomerCtrl', ['$scope', '$routeParams',
    function ($scope, $routeParams) {
        // Parse the customer name and city out of the URL via $routeParams.
        $scope.customerName = $routeParams.customer;
        $scope.customerCity = $routeParams.city;
    }]);

})();
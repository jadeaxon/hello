'use strict';

(function() {

    var app = angular.module('helloWorld.app', [
        'ngRoute', // Build in AngularJS module that does client-side URL routing.
        'helloWorld.controllers' // Our custom controllers.

    ]);

    // Route various URL requests directly back to our app.
    // This prevents HTTP requests to the server.
    // The routing associates a controller with a view/template/partial.
    // This pair replaces the ng-view tagged DOM element in index.html.
    // Parts of the URL can be parsed out into "route parameters" which the controller can access via $routeParams.
    app.config(['$routeProvider', '$locationProvider',
        function ($routeProvider, $locationProvider) {
            $routeProvider.when('/', {
                templateUrl: 'partials/main.html',
                controller: 'MainCtrl'
            }).when('/show', {
                templateUrl: 'partials/show.html',
                controller: 'ShowCtrl'
            }).when('/customer', {
                templateUrl: 'partials/customer.html',
                controller: 'CustomerCtrl'
            }).when('/addCustomer', {
                templateUrl: 'partials/newCustomer.html',
                controller: 'AddCustomerCtrl'
            }).when('/addedCustomer/:customer/:city', {
                // The above makes it so we can get customer and city via $routeParams.
                templateUrl: 'partials/addedCustomer.html',
                controller: 'AddedCustomerCtrl'
            });

            // Forces us to use !#/ prefix before locally routed URLs.
            // I think this is only necessary for compatibility with older browsers.
            $locationProvider.html5Mode(false).hashPrefix('!');
        }]);

})();


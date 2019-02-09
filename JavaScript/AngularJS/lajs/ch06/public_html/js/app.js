'use strict';

var blogApp = angular.module('blog.app', [
    'ngRoute',     
    'blog.controllers',
    'blog.services' // Allows each service to be injected into any controller.
    
]);

blogApp.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider.
                when('/', {
                    templateUrl: 'partials/main.html',
                    controller: 'BlogCtrl'
                }).when('/blogPost/:id', {
                    templateUrl: 'partials/blogPost.html',
                    controller: 'BlogViewCtrl'
                });

        $locationProvider.html5Mode(false).hashPrefix('!');
    }]);




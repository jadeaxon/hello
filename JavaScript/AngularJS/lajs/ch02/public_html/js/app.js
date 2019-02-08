'use strict';

// This is the application module.
// We bind this to <html> via ng-app.
var helloWorldApp = angular.module(
    'helloWorldApp', // The name of our app module.
    // The other modules it depends on.
    // ngRoute lets us do client-side routing of HTML templates/partials to ng-view via URL fragments.
    // We've factored out our custom controllers into another module to be, well, modular.
    ['ngRoute', 'helloWorldControllers']
);

// Service names start with $.  To inject them in a way that won't break if this code is minified, we use
// the syntax that puts the service names in an array.
helloWorldApp.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider.
                when('/', {
                    // Use the main partial view template for our base URL.
                    templateUrl: 'partials/main.html',
                    controller: 'MainCtrl'
                }).when('/show', {
                    // Route to the "show" partial view template for <base URL>/show.
                    // Note that you can register a different controller to handle the new view.
                    templateUrl: 'partials/show.html',
                    controller: 'ShowCtrl'
                });

        // This forces us to use the #! syntax for URL fragments to route by.
        // You can get more natural-looking URLs using the HTML 5 mode, but not all browsers support it.
        $locationProvider.html5Mode(false).hashPrefix('!');
    }]);




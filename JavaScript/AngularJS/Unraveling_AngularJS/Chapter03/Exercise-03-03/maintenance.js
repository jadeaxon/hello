angular.module('maintenance', ['ngRoute'])
  .controller('adminCtrl', AdminCtrl)
  .config(function ($routeProvider) {
    $routeProvider.when('/locations', {
      templateUrl: 'views/locations.html'
    });
    $routeProvider.when('/sites', {
      templateUrl: 'views/sites.html'
    });
    $routeProvider.otherwise({
      templateUrl: 'views/main.html'
    });
  });

function AdminCtrl($scope) {
}

angular.module('main', ['ngRoute', 'core', 'maintenance'])
  .controller('adminCtrl', AdminCtrl)
  .controller('mainCtrl', MainCtrl)
  .config(function ($routeProvider) {
    $routeProvider.when('/locations', {
      templateUrl: 'views/locations.html'
    });
    $routeProvider.when('/sites', {
      templateUrl: 'views/sites.html',
      controller: 'sitesCtrl'
    });
    $routeProvider.when('/types', {
      templateUrl: 'views/types.html',
      controller: 'typesCtrl'
    });
    $routeProvider.otherwise({
      templateUrl: 'views/main.html',
      controller: 'mainCtrl'
    });
  });

function AdminCtrl($scope, currentSpot) {
  $scope.isActive = isActive;
  $scope.getTitle = getTitle;
  $scope.getActiveMenu = getActiveMenu;

  function isActive(menuId) {
    return currentSpot.getActiveMenu() == menuId;
  }

  function getTitle() {
    return currentSpot.getTitle();
  }

  function getActiveMenu() {
    return currentSpot.getActiveMenu();
  }
}

function MainCtrl(currentSpot) {
}

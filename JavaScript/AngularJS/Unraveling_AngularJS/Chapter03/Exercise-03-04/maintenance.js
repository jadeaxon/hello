angular.module('maintenance', ['ngRoute'])
  .controller('adminCtrl', AdminCtrl)
  .controller('mainCtrl', MainCtrl)
  .controller('locationsCtrl', LocationsCtrl)
  .controller('sitesCtrl', SitesCtrl)
  .factory('currentSpot', currentSpot)
  .config(function ($routeProvider) {
    $routeProvider.when('/locations', {
      templateUrl: 'views/locations.html',
      controller: 'locationsCtrl'
    });
    $routeProvider.when('/sites', {
      templateUrl: 'views/sites.html',
      controller: 'sitesCtrl'
    });
    $routeProvider.otherwise({
      templateUrl: 'views/main.html',
      controller: 'mainCtrl'
    });
  });

function AdminCtrl($scope, currentSpot) {
  $scope.isActive = isActive;
  $scope.getTitle = getTitle;

  function isActive(menuId) {
    return currentSpot.getActiveMenu() == menuId;
  }

  function getTitle() {
    return currentSpot.getTitle();
  }
}

function currentSpot() {
  var activeMenuId = '';
  var titleText = '';

  return {
    setCurrentSpot: function (menuId, title) {
      activeMenuId = menuId;
      titleText = title;
    },
    getActiveMenu: function () {
      return activeMenuId;
    },
    getTitle: function () {
      return titleText;
    }
  }
}

function MainCtrl(currentSpot) {
  currentSpot.setCurrentSpot('', '')
}

function LocationsCtrl(currentSpot) {
  currentSpot.setCurrentSpot('Locations',
    'Manage the list of diving locations')
}

function SitesCtrl(currentSpot) {
  currentSpot.setCurrentSpot('Sites',
    'Manage the list of dive sites')
}


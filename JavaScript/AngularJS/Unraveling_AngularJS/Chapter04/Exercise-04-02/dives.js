angular.module('diveLog', [])
  .controller('diveLogCtrl', DiveLogCtrl)
  .factory('diveLogApi', diveLogApi);

function DiveLogCtrl($scope, diveLogApi) {
  $scope.dives = [];
  $scope.isLoading = isloading;
  $scope.refreshDives = refreshDives;

  var loading = false;

  function isloading() {
    return loading;
  }

  function refreshDives() {
    loading = true;
    $scope.dives = [];
    setTimeout(function () {
      $scope.dives = diveLogApi.getDives();
      loading = false;
      $scope.$apply();
    }, 1000);
  }
}

function diveLogApi() {
  var dives = [
    {
      site: 'Abu Gotta Ramada',
      location: 'Hurghada, Egypt',
      depth: 72,
      time: 54
    },
    {
      site: 'Ponte Mahoon',
      location: 'Maehbourg, Mauritius',
      depth: 54,
      time: 38
    },
    {
      site: 'Molnar Cave',
      location: 'Budapest, Hungary',
      depth: 98,
      time: 62
    }];

  return {
    getDives: function () {
      return dives;
    }
  };
}

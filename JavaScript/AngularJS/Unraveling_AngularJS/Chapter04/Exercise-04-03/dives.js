angular.module('diveLog', [])
  .controller('diveLogCtrl', DiveLogCtrl)
  .factory('diveLogApi', diveLogApi);

function DiveLogCtrl($scope, diveLogApi) {
  $scope.dives = [];
  $scope.errorMessage = '';
  $scope.isLoading = isloading;
  $scope.refreshDives = refreshDives;

  var loading = false;

  function isloading() {
    return loading;
  }

  function refreshDives() {
    loading = true;
    $scope.dives = [];
    $scope.errorMessage = '';
    diveLogApi.getDives().then(
      function (data) {
        // --- Resolved handler
        $scope.dives = data;
        loading = false;
      },
      function (reason) {
        // --- Rejected handler
        $scope.errorMessage = reason
        loading = false;
    });
  }
}

function diveLogApi($q) {
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

  var counter = 0;

  return {
    getDives: function () {
      var deferred = $q.defer();
      counter++;
      setTimeout(function () {
        if (counter % 3 == 0) {
          deferred.reject('Error: Call counter is '
            + counter);
        } else {
          deferred.resolve(dives);
        }
      }, 1000);
      return deferred.promise;
    }
  };
}

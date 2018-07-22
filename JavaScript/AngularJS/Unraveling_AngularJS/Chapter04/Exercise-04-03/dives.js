angular.module('diveLog', [])
  .controller('diveLogCtrl', DiveLogCtrl)
  .factory('$$diveLogApi', DiveLogApi);

function DiveLogCtrl($scope, $$diveLogApi) {
  $scope.dives = [];
  $scope.errorMessage = '';
  $scope.isLoading = isloading;
  $scope.refreshDives = refreshDives;

  // Show the spinny progress wheel if this is true.
  var loading = false;

  function isloading() {
    return loading;
  }

  function refreshDives() {
    loading = true;
    $scope.dives = [];
    $scope.errorMessage = '';

    // Injected service that simulates an Ajax call.
    // getDives() starts an async operation and returns a promise.
    // We use then() to register functions to deal with promise resolution or rejection.
    $$diveLogApi.getDives().then(
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

// Factory function for a service that uses the $q service to run
// async code and return promises.
function DiveLogApi($q) {
  // The data model.  In the future, we'll load this async from the server.
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

  // The service singleton.
  return {
    getDives: function () {
      var deferred = $q.defer(); // Create a promise.
      counter++;
      // Run some async code once.
      setTimeout(function () {
        // Simulate an error every 3rd time the Refresh button is pressed.
        if (counter % 3 == 0) {
          // This signals the rejection function we register with promise.then().
          deferred.reject('Error: Call counter is ' + counter);
        }
        else {
          // This signals the resolution function we register with promise.then().
          deferred.resolve(dives);
        }
      }, 1000);
      // The deferred task has a promise we can return so that we can register rejection/resolution
      // handlers via promise.then().
      return deferred.promise;
    } // getDrives()
  }; // service singleton
} // DriveLogApi() service factory




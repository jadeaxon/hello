angular.module('maintenance')
  .factory('locationsApi', locationsApi)
  .controller('locationsCtrl', LocationsCtrl);

function locationsApi($q) {
  var defaultLocations = [
    { id: 1, displayName: 'Hurghada, Egypt' },
    { id: 2, displayName: 'Ecsed, Hungary' },
    { id: 3, displayName: 'Maehbourg, Mauritius' }
  ];

  var locations = defaultLocations;

  function getLocationIndexById(id) {
    for (var i = 0; i < locations.length; i++) {
      if (locations[i].id == id) {
        return i;
      }
    }
    return -1;
  }

  function defer(time, operation) {
    var deferred = $q.defer();
    setTimeout(function () {
      var result = operation();
      deferred.resolve(result);
    }, time);
    return deferred.promise;
  }

  return {
    getLocations: function () {
      return defer(100, function () {
        return locations.slice(0);
      })
    },
    getLocationById: function (id) {
      return defer(10, function () {
        var itemId = getLocationIndexById(id);
        if (itemId >= 0) {
          return locations[itemId];
        } else {
          return null;
        }
      })
    },
    addLocation: function (location) {
      return defer(1000, function () {
        var newId = locations.length + 1;
        location.id = newId;
        locations.push(location);
      })
    },
    removeLocation: function (id) {
      return defer(1000, function () {
        var itemId = getLocationIndexById(id);
        if (itemId >= 0) {
          locations.splice(itemId, 1);
        }
      })
    },
    updateLocation: function (location) {
      return defer(1000, function () {
        var itemId = getLocationIndexById(location.id);
        if (itemId >= 0) {
          locations[itemId] = location;
        }
      })
    }
  }
}

function LocationsCtrl($scope, locationsApi) {
  var selectedId = -1;
  var addFlag = false;
  var editFlag = false;
  var removeFlag = false;
  var rings = [];

  $scope.model = {};
  $scope.isBusy = isBusy;
  $scope.isLoading = isLoading;
  $scope.startAdd = startAdd;
  $scope.startEdit = startEdit;
  $scope.startRemove = startRemove;
  $scope.cancel = reset;
  $scope.isInReadMode = isInReadMode;
  $scope.isInAddMode = isInAddMode;
  $scope.isInEditMode = isInEditMode;
  $scope.isInRemoveMode = isInRemoveMode;
  $scope.add = add;
  $scope.save = save;
  $scope.remove = remove;

  refresh();

  function isBusy(id) {
    if (angular.isDefined(id)) {
      return rings.indexOf(id) >= 0;
    } else {
      return rings.length > 0;
    }
  }

  function isLoading() {
    return isBusy(-2);
  }

  function startAdd() {
    reset();
    selectedId = -1;
    addFlag = true;
    $scope.model.locationBox = '';
  }

  function startEdit(id) {
    reset();
    selectedId = id;
    editFlag = true;
    var item;
    locationsApi.getLocationById(id)
      .then(function (data) {
        item = data;
        $scope.model.locationBox = item.displayName;
      });
  }

  function startRemove(id) {
    reset();
    selectedId = id;
    removeFlag = true;
  }

  function reset() {
    selectedId = -1;
    addFlag = false;
    editFlag = false;
    removeFlag = false;
  }

  function isInReadMode(id) {
    return selectedId < 0 || selectedId != id;
  }

  function isInAddMode() {
    return addFlag;
  }

  function isInEditMode(id) {
    return selectedId == id && editFlag;
  }

  function isInRemoveMode(id) {
    return selectedId == id && removeFlag;
  }

  function add() {
    useBackend(-1, function () {
      return locationsApi.addLocation(
        {
          id: 0,
          displayName: $scope.model.locationBox
        })
    })
  }

  function save() {
    useBackend(selectedId, function () {
      return locationsApi.updateLocation(
        {
          id: selectedId,
          displayName: $scope.model.locationBox
        })
    })
  }

  function remove(id) {
    useBackend(id, function () {
      return locationsApi.removeLocation(id);
    })
  }

  function busy(id) {
    if (isBusy(id)) {
      return;
    }
    rings.push(id);
  }

  function complete(id) {
    var idx = rings.indexOf(id);
    if (idx < 0) {
      return;
    }
    rings.splice(idx, 1);
  }

  function refresh() {
    busy(-2);
    locationsApi.getLocations()
      .then(function (data) {
        $scope.locations = data;
        complete(-2);
      });
    reset();
  }

  function useBackend(id, operation) {
    busy(id);
    operation().then(
      function (data) {
        refresh();
        complete(id);
      });
  }
}
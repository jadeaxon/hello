angular.module('maintenance')
  .factory('locationsApi', locationsApi)
  .controller('locationsCtrl', LocationsCtrl)
  .constant('apiUrl',
    'http://unraveling-ng.azurewebsites.net/api/dive/location/')
  .constant('userId',
    '1569c635-614d-46b9-bbeb-44fa1c5abcde')
  .constant('userSecret',
    'a7bcc9beada3468c8e1ba8b142494ef4cdce198d0c904f91a643839e4a69fa17ceedffb28e3e4328abd026b6dbfabcde');

function locationsApi($http, apiUrl,
  userId, userSecret) {

  function get(param) {
    return request("GET", param);
  }

  function post(data) {
    return request("POST", null, data);
  }

  function put(data) {
    return request("PUT", null, data);
  }

  function del(param) {
    return request("DELETE", param);
  }

  function request(verb, param, data) {
    var req = {
      method: verb,
      url: url(param),
      headers: {
        'Authorization': getAuthHeader()
      },
      data: data
    }
    return $http(req);
  }

  function url(param) {
    if (param == null || !angular.isDefined(param)) {
      param = '';
    }
    return apiUrl + param;
  }

  function getAuthHeader() {
    return "TenantSecret "
      + userId + "," + userSecret;
  }

  return {
    getLocations: function () {
      return get();
    },
    getLocationById: function (id) {
      return get(id)
    },
    addLocation: function (location) {
      return post(location)
    },
    removeLocation: function (id) {
      return del(id)
    },
    updateLocation: function (location) {
      return put(location)
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
  $scope.errorMessage = '';
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
  $scope.hasError = hasError;

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
    for (var i = 0; i < $scope.locations.length; i++) {
      var item = $scope.locations[i];
      if (item.id == id) {
        $scope.model.locationBox = item.displayName;
      }
    }
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
    $scope.errorMessage = '';
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

  function hasError() {
    return $scope.errorMessage != '';
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
      .success(function (data) {
        $scope.locations = data;
        complete(-2);
        $scope.errorMessage = '';
      })
      .error(
        function (errorInfo, status) {
          setError(errorInfo, status, -2)
        });

    reset();
  }

  function useBackend(id, operation) {
    busy(id);
    $scope.errorMessage = '';
    operation()
      .success(
        function (data) {
          refresh();
          complete(id);
        })
      .error(
        function (errorInfo, status) {
          setError(errorInfo, status, id)
        });
  }

  function setError(errorInfo, status, id) {
    reset();
    complete(id);
    if (status == 401) {
      $scope.errorMessage = "Authorization failed."
    } else if (angular.isDefined(errorInfo.reasonCode)
        && errorInfo.reasonCode == "TenantLimitExceeded")
    {
      $scope.errorMessage =
          "You cannot add more locations.";
    } else {
      $scope.errorMessage = errorInfo.message;
    }
  }
}
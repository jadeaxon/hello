angular.module('yw.planning', [])
  .factory('plannerSrv', plannerService)
  .factory('messageSrv', messageService)
  .controller('planCtrl', PlanController);

function plannerService() {
  return {
    isDeep: function(depth){
      return depth > 60;
    }
  }
}

function messageService() {
  return {
    certMessage: function (isDeep) {
      return isDeep
        ? "You need an advanced diving certification."
        : "This depth is shallow enough to take.";
    }
  }
}

function PlanController($scope, plannerSrv,
  messageSrv) {
  $scope.maxDepth = 30;
  $scope.needAdvancedCert = function () {
    return plannerSrv.isDeep(
      $scope.maxDepth);
  };
  $scope.message = function () {
    return messageSrv.certMessage(
      plannerSrv.isDeep($scope.maxDepth));
  }
}
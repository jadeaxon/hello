angular.module('yw.planning', [])
  .factory('plannerSrv', plannerService)
  .factory('messageSrv', messageService)
  .controller('planCtrl', ['$scope', 'plannerSrv',
    'messageSrv', PlanController]);

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

function PlanController($scope, pSrv, mSrv) {
  $scope.maxDepth = 30;
  $scope.needAdvancedCert = function () {
    return pSrv.isDeep(
      $scope.maxDepth);
  };
  $scope.message = function () {
    return mSrv.certMessage(
      pSrv.isDeep($scope.maxDepth));
  }
}
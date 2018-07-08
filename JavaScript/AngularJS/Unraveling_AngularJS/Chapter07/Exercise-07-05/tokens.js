angular.module('token', [])
  .constant('initialGoal', 8)
  .controller('tokenGoalCtrl',
    function ($scope, initialGoal) {
      $scope.divers = [
        "Bob", "Cecile", "Jake"
      ];
      $scope.tokens = initialGoal;
      $scope.increment = function () {
        $scope.tokens++;
      }
      $scope.decrement = function () {
        $scope.tokens--;
      }
    })
  .controller('tokenCollCtrl',
    function ($scope, initialGoal) {
      $scope.toGet = initialGoal;
      $scope.collected = 0;
      $scope.hasEnough = function () {
        return $scope.toGet <= $scope.collected;
      }
    })
  .controller('diverCtrl',
    function ($scope) {
      $scope.tokensFound = 0;
      $scope.found = function () {
        $scope.tokensFound++;
      }
      $scope.lost = function () {
        $scope.tokensFound--;
      }
    });

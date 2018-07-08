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
        goalChanged();
      }

      $scope.decrement = function () {
        $scope.tokens--;
        goalChanged();
      }

      function goalChanged() {
        $scope.$broadcast('NewGoal', $scope.tokens);
      }
    })
  .controller('tokenCollCtrl',
    function ($scope, initialGoal) {
      $scope.toGet = initialGoal;
      $scope.collected = 0;
      $scope.hasEnough = function () {
        return $scope.toGet <= $scope.collected;
      }

      $scope.$on('NewGoal',
        function (event, newGoal) {
          $scope.toGet = newGoal;
      });

      $scope.$on('TokenChange',
        function (event, diff) {
          $scope.collected += diff;
      })
    })
  .controller('diverCtrl',
    function ($scope) {
      $scope.tokensFound = 0;
      $scope.found = function () {
        $scope.tokensFound++;
        tokenChanged(1);
      }
      $scope.lost = function () {
        $scope.tokensFound--;
        tokenChanged(-1);
      }

      function tokenChanged(diff) {
        $scope.$emit('TokenChange', diff)
      }
    });

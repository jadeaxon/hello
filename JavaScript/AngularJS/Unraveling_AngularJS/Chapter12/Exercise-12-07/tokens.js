angular.module('token', [])
  .constant('initialGoal', 10)
  .controller('tokenGameCtrl', TokenGameCtrl)
  .directive('diverPanel', DiverPanel);

function TokenGameCtrl($scope, initialGoal) {
  $scope.divers = [
    "Bob", "Cecile", "Jake"
  ];

  $scope.toCollect = initialGoal;
  $scope.collected = 0;

  $scope.hasEnough = function () {
    return $scope.toCollect <= $scope.collected;
  }
}

function DiverPanel() {
  return {
    scope: {
      diver: '@diverName',
      allFound: '=counter'
    },
    templateUrl: 'diverPanel.html',
    link: function (scope, element, attrs) {
      scope.tokensFound = 0;
      scope.diver = attrs['diverName'];

      scope.found = function () {
        scope.tokensFound++;
        scope.allFound++;
      }

      scope.lost = function () {
        scope.tokensFound--;
        scope.allFound--;
      }
    }
  }
}

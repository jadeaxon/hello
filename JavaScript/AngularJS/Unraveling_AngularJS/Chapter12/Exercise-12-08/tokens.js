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
  $scope.tokens = [];

  $scope.change = function (found) {
    $scope.collected += found;
    $scope.tokens.push(found);
  }

  $scope.hasEnough = function () {
    return $scope.toCollect <= $scope.collected;
  }
}

function DiverPanel() {
  return {
    scope: {
      diver: '@diverName',
      sign: '&change'
    },
    templateUrl: 'diverPanel.html',
    link: function (scope, element, attrs) {
      scope.tokensFound = 0;
      scope.diver = attrs['diverName'];

      scope.found = function () {
        scope.tokensFound++;
        scope.sign({ found: 1 });
      }

      scope.lost = function () {
        scope.tokensFound--;
        scope.sign({ found: -1 });
      }
    }
  }
}

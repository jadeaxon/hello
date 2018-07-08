angular.module('watcher', [])
  .controller('divesCtrl', function ($scope) {
    $scope.dives = [
      { site: 'El Aroukh', depth: 32 },
      { site: 'Abu Ramada', depth: 112 },
      { site: 'Small Giftun', depth: 54 }
    ];

    var canEval = false;

    $scope.clone = clone
    $scope.swapItems = swapItems;
    $scope.changeItemProp = changeItemProp;
    $scope.reset = reset;
    $scope.detected = detected;

    $scope.$watch('dives', function () {
      $scope.byRef = canEval;
    });
    $scope.$watchCollection('dives', function () {
      $scope.byColl = canEval;
    });
    $scope.$watch('dives', function () {
      $scope.byVal = canEval;
    }, true);

    $scope.reset();

    function clone() {
      $scope.reset();
      canEval = true;
      $scope.dives = $scope.dives.slice(0);
    }

    function swapItems() {
      $scope.reset();
      canEval = true;
      var temp = $scope.dives[0];
      $scope.dives[0] = $scope.dives[1];
      $scope.dives[1] = temp;
    }

    function changeItemProp() {
      $scope.reset();
      canEval = true;
      $scope.dives[0].depth++;
    }

    function reset() {
      $scope.byRef = false;
      $scope.byColl = false;
      $scope.byVal = false;
    }

    function detected(flag) {
      return flag ? "label-success"
        : "label-danger";
    }
  });
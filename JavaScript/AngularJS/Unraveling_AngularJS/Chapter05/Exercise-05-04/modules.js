angular.module('yw.main',
  [
    'my.core',
    'yw.divelog',
    'yw.user',
    'yw.charts'
  ]);

angular.module('yw.divelog', []);

angular.module('yw.user', ['my.core']);

angular.module('my.core',
  [
    'my.core.comm',
    'my.core.ui'
  ]);

angular.module('yw.charts', ['my.core']);

angular.module('my.core.comm', []);
angular.module('my.core.ui', []);

angular.module('yw.main')
  .controller('moduleCtrl',
    function ($scope) {
      $scope.message =
        'Module dependency checked.';
    });
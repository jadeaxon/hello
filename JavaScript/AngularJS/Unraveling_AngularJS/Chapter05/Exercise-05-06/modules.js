angular.module('yw.main',
  [
    'my.core',
    'yw.divelog',
    'yw.user',
    'yw.charts'
  ])
  .config(function () {
    console.log('yw.main: config()');
  })
  .run(function () {
    console.log('yw.main: run()');
  });

angular.module('yw.divelog', [])
  .config(function () {
    console.log('yw.divelog: config()');
  })
  .run(function () {
    console.log('yw.divelog: run()');
  });

angular.module('yw.user', ['my.core'])
  .config(function () {
    console.log('yw.user: config()');
  })
  .run(function () {
    console.log('yw.user: run()');
  });

angular.module('my.core',
  [
    'my.core.comm',
    'my.core.ui'
  ])
  .config(function () {
    console.log('my.core: config()');
  })
  .run(function () {
    console.log('my.core: run()');
  });

angular.module('yw.charts', ['my.core'])
  .config(function () {
    console.log('yw.charts: config() #1');
  })
  .run(function () {
    console.log('yw.charts: run() #1');
  })
  .run(function () {
    console.log('yw.charts: run() #2');
  })
  .config(function () {
    console.log('yw.charts: config() #2');
  })

angular.module('my.core.comm', [])
  .config(function () {
    console.log('my.core.comm: config()');
  })
  .run(function () {
    console.log('my.core.comm: run()');
  });

angular.module('my.core.ui', [])
  .config(function () {
    console.log('my.core.ui: config()');
  })
  .run(function () {
    console.log('my.core.ui: run()');
  });

angular.module('yw.main')
  .controller('moduleCtrl',
    function ($scope) {
      $scope.message =
        'Module dependency checked.';
    });
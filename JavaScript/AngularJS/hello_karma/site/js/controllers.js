(function() {

var controllers = angular.module('karma.controllers', []);

controllers.controller('MainCtrl', function($scope) {
  $scope.message = 'Hello, Karma!';
});


})();
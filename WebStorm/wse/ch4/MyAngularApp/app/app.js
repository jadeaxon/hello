angular.module('app', ['ngRoute', 'app.controllers'])
    .config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/', {
            templateUrl: 'app/views/entries.html',
            controller: 'EntriesController'
        }).when('/entry/:id', {
            templateUrl: 'app/views/entry.html',
            controller: 'EntryController'
        }).when('/menu/:id', {
            templateUrl: 'app/views/menu.html',
            controller: 'MenuController'
        }).otherwise({
            redirectTo: '/'
        });
    }]);

angular.module('app.controllers', ['app.directives'])
    .controller('EntriesController', ['$scope', '$http', function($scope, $http){
        $http.get('jsondata/entries.json').success(function(data){
            $scope.entries = data;
        });
    }])
    .controller('EntryController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
        $http.get('jsondata/entries.json').success(function(data){
            $scope.entry = data[$routeParams.id];
        });
    }])
    .controller('MenuController', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams){
        $http.get('jsondata/menu.json').success(function(data){
            $scope.item = data[$routeParams.id];
        });
    }]);

angular.module('app.directives', [])
    .directive('navbar', [function(){
        return {
            controller: ['$scope', '$http', function($scope, $http){
                $http.get('jsondata/menu.json').success(function(data){
                    $scope.menu = data;
                });
            }],
            restrict: 'E',
            templateUrl: 'app/partials/navbar.html',
            replace: true
        };
    }]);

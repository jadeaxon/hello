var app = angular.module("helloApp", []);

// Technically, we're defining a controller type and providing its constructor function.
// So, the type name should be uppercase.
app.controller("HelloCtrl", function ($scope) {
    // The scope is the view model.
    // AngularJS provides two-way data binding between the scope and the view (DOM elements).
    $scope.message = "Hello, AngularJS!";
});

// An app can have many controllers.  They can be linked to different DOM elements.
app.controller("NameCtrl", function ($scope) {
    $scope.firstName = "Jeff";
    $scope.lastName = "Anderson";

    // A scope can have methods.
    $scope.fullName = function () {
        return $scope.firstName + " " + $scope.lastName;
    };

    // By calling this, we'll be able to see that we can have multiple instances of the same controller type.
    // Each instance will have its own separate scope.
    $scope.setFirstName = function(firstName) {
      $scope.firstName = firstName;
    };

});


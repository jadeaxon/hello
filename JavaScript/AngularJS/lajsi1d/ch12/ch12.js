var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.chapter = 12;
  $scope.topic = "Custom Directives"
  $scope.message = "This is chapter " + $scope.chapter + ".";


});

// Define a custom attribute directive.
// If we apply jsa-title to any element, it will replace it with the HTML template.
// jsaTitle => jsa-title in the HTML.
app.directive("jsaTitle", function (){
  return {
    // Note that the directive has access to its parent element's scope.
    template: "<h2 id='jsa-title'>Chapter {{chapter}}: {{topic}}</h2>"
  };
});
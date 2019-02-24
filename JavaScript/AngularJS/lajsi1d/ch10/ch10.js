var app = angular.module("app", []);

app.controller("MainCtrl", function ($scope) {
  $scope.message = "This is chapter 8."

  $scope.person = {
    name: "Frodo Baggins",
    height: "3'4\"",
    home: "The Shire",
    money: 1234567890.0987654321
  };

});

// Define a custom filter.
app.filter("append", function () {
  function _appendFilter(input) {
    return input + "__filtered";
  }
  return _appendFilter;
});

// Define a custom filter that takes two args.
// Note that we can inject the filter service to define filters in terms of other filters.
app.filter("surround", function ($filter) {
  function _surroundFilter(input, left, right) {
    var lc = $filter('lowercase'); // Returns a filter function.
    return lc(left) + input + lc(right);
  }
  return _surroundFilter;
});

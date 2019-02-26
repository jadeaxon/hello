// Edited externally in gVim.
var app = angular.module('karma.app', ['karma.controllers']);

app.directive("jsaTitle", function () {
  return {
    template: "<h2 class='jsa-title'>{{message}}</h2>",
    restrict: "E"
  };
});

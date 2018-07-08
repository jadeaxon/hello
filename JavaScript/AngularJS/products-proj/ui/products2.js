var deps = ["ngResource", "ngRoute", "increment"];
var app = angular.module("exampleApp", deps);

// Calling constant() actually creates a service you have to inject.
app.constant("baseUrl", "http://localhost:2403/products/");

// Route URLs to views.
// The $routeProvider provides/configs the $route service.
// The $locationProvider provides/configs the $location service.
// The route mappings determine what is displayed by <ng-view>.
app.config(function ($routeProvider, $locationProvider) {
  // This allows cleaner URLs in modern browsers.
  $locationProvider.html5Mode(true);

  $routeProvider.when("/list", {
    templateUrl: "/tableView.html"
  });

  $routeProvider.when("/edit", {
    templateUrl: "/editorView.html"
  });

  $routeProvider.when("/create", {
    templateUrl: "/editorView.html"
  });

  $routeProvider.otherwise({
    templateUrl: "/tableView.html"
  });
});

app.controller("defaultCtrl", function ($scope, $http, $resource, $location, baseUrl) {
  // This holds a newly created product or copy of product being edited.
  $scope.currentProduct = null;

  // Did we have an Ajax error?
  $scope.error = null;

  // Define products resource.
  // The 2nd : separates the variable part of the URL from the fixed part.
  // The 2nd arg says to bind the id part of the URL to the id property of the object.
  // In a more complex API, you might need to bind multiple URL parts to object properties.
  // The 3rd arg maps resource actions to HTTP methods.
  // The use here makes it more compatible with Deployd REST APIs.
  $scope.productsResource = $resource(
    baseUrl + ":id",
    { id: "@id" },
    { create: { method: "POST" }, save: { method: "PUT" }}
  );

  // Uses $resource service to load the product data.
  // Your Deployd server needs to be running at the given port in baseUrl.
  $scope.listProducts = function () {
    // This populates the list with a bunch of Resource objects.
    // These Resource objects have special methods like $delete() and $save().
    $scope.products = $scope.productsResource.query();

    // If you need to do something immediately when the data loads, use the $promise property.
    $scope.products.$promise.then(function (data) {
      // This happens before the scope data binding events fire.
      console.log("Just got the data.");
    });
  };

  // Deletes a product.  There's a delete button in each row that triggers this.
  $scope.deleteProduct = function (product) {
    // Why does this work?
    // Here product is actually a Resource object which has an async $delete() method.
    // You can attach a success promise to the deferred delete to update browser scope data.
    product.$delete().then(
      function () {
        $scope.products.splice($scope.products.indexOf(product), 1);
      }
    );
    // This will cause <ng-view> to change base on the $route config.
    $location.path("/list");
  };

  // Adds a new product to the product list.
  $scope.createProduct = function (product) {
    // We use new to create a new product resource object based on a plain product object.
    // We then do a deferred save on that resource with a promise to update the browser data
    // when the deferred save succeeds.
    //
    // This turns any plain product objects that get added to the collection into resource
    // objects so that all the special $save(), $delete(), etc. methods can be called on them.
    // Since $save() uses PUT by default, we had to map new resource action $create() to POST.
    new $scope.productsResource(product).$create().then(
      function (newProduct) {
        // Hmmm, are we getting back a plain product here or a product resource?
        $scope.products.push(newProduct);

        // This will cause <ng-view> to change base on the $route config.
        $location.path("/list");
      }
    );
  };

  // Updates a product.
  $scope.updateProduct = function (product) {
    // The product resource object has a special $save() method.
    product.$save();

    // This will cause <ng-view> to change base on the $route config.
    $location.path("/list");
  };

  // Edits or creates a product.
  $scope.editOrCreateProduct = function (product) {
    $scope.currentProduct = product ? product : {};

    // This will cause <ng-view> to change base on the $route config.
    $location.path("/edit");
  };

  // Saves product edit.
  $scope.saveEdit = function (product) {
    if (angular.isDefined(product.id)) {
      $scope.updateProduct(product);
    }
    else {
      $scope.createProduct(product);
    }
    $scope.currentProduct = {};
  };

  // Cancels product edit.
  $scope.cancelEdit = function () {
    if ($scope.currentProduct && $scope.currentProduct.$get) {
      $scope.currentProduct.$get();
    }
    // Shouldn't this be in an else clause?
    // No, currentProduct is acting as an object ref.
    $scope.currentProduct = {};

    // This will cause <ng-view> to change base on the $route config.
    $location.path("/list");
  };

  // Create the initial list of products.
  $scope.listProducts();
});



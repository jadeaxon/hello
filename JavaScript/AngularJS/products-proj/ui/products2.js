var app = angular.module("exampleApp", ["ngResource", "increment"]);

// Calling constant() actually creates a service you have to inject.
app.constant("baseUrl", "http://localhost:2403/products/");

app.controller("defaultCtrl", function ($scope, $http, $resource, baseUrl) {
  // Choose whether we show the product listing or product edit view.
  $scope.displayMode = "list";

  // This holds a newly created product or copy of product being edited.
  $scope.currentProduct = null;

  // Did we have an Ajax error?
  $scope.error = null;

  // Define products resource.
  // The 2nd : separates the variable part of the URL from the fixed part.
  // The 2nd arg says to bind the id part of the URL to the id property of the object.
  // In a more complex API, you might need to bind multiple URL parts to object properties.
  $scope.productsResource = $resource(baseUrl + ":id", { id: "@id" });

  // Uses $resource service to load the product data.
  // Your Deployd server needs to be running at the given port in baseUrl.
  $scope.listProducts = function () {
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
    product.$delete().then(
      function () {
        $scope.products.splice($scope.products.indexOf(product), 1);
      }
    );
    $scope.displayMode = "list";
  };

  // Adds a new product to the product list.
  $scope.createProduct = function (product) {
    new $scope.productsResource(product).$save().then(function(newProduct) {
      $scope.products.push(newProduct);
      $scope.displayMode = "list";
    });
  };

  // Updates a product.
  $scope.updateProduct = function (product) {
    product.$save();
    $scope.displayMode = "list";
  };

  // Edits or creates a product.
  $scope.editOrCreateProduct = function (product) {
    $scope.currentProduct = product ? product : {};
    $scope.displayMode = "edit";
  };

  // Saves product edit.
  $scope.saveEdit = function (product) {
    if (angular.isDefined(product.id)) {
      $scope.updateProduct(product);
    }
    else {
      $scope.createProduct(product);
    }
  };

  // Cancels product edit.
  $scope.cancelEdit = function () {
    if ($scope.currentProduct && $scope.currentProduct.$get) {
      $scope.currentProduct.$get();
    }
    $scope.currentProduct = {};
    $scope.displayMode = "list";
  };

  // Create the initial list of products.
  $scope.listProducts();
});



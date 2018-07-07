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
  $scope.productsResource = $resource(baseUrl + ":id", { id: "@id" });

  // Uses $resource service to load the product data.
  // Your Deployd server needs to be running at the given port in baseUrl.
  $scope.listProducts = function () {
    $scope.products = $scope.productsResource.query();
  }

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
    var deferred = $http.post(baseUrl, product);
    deferred.then(
      function (response) {
        // Update list in browser if server update succeeds.
        $scope.products.push(response.data);
        $scope.displayMode = "list";
      },
      function (error) {
        $scope.error = error;
      }
    );
  }

  // Updates an existing product.
  $scope.updateProduct = function (product) {
    var deferred = $http({
      url: baseUrl + product.id,
      method: "PUT",
      data: product
    });
    deferred.then(
      function (response) {
        // Update product in browser after server update succeeds.
        var modifiedProduct = response.data;
        for (var i = 0; i < $scope.products.length; i++) {
          if ($scope.products[i].id == modifiedProduct.id) {
            $scope.products[i] = modifiedProduct;
            break;
          }
        } // next product
        $scope.displayMode = "list";
      },
      function (error) {
        $scope.error = error;
      }
    ); // then
  }; // updateProduct

  // Creates a new product or edits an existing product.
  // Uses a copy of the product when editing existing so cancel works.
  // Switches the UI to edit view.
  $scope.editOrCreateProduct = function (product) {
    $scope.currentProduct = product ? angular.copy(product) : {};
    $scope.displayMode = "edit";
  };

  // Saves new/edit product to products list.
  $scope.saveEdit = function (product) {
    if (angular.isDefined(product.id)) {
      $scope.updateProduct(product);
    }
    else {
      $scope.createProduct(product);
    }
  };

  // Cancels edit.  Goes back to products listing view.
  $scope.cancelEdit = function () {
    $scope.currentProduct = {};
    $scope.displayMode = "list";
  };

  // Create the initial list of products.
  $scope.listProducts();
});



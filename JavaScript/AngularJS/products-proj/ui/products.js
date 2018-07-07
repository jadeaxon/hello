var app = angular.module("exampleApp", []);
app.controller("defaultCtrl", function ($scope) {
  // Choose whether we show the product listing or product edit view.
  $scope.displayMode = "list";

  // This holds a newly created product or copy of product being edited.
  $scope.currentProduct = null;

  // Creates the list of dummy products.
  $scope.listProducts = function () {
    $scope.products = [
      { id: 0, name: "Dummy1", category: "Test", price: 1.25 },
      { id: 1, name: "Dummy2", category: "Test", price: 2.45 },
      { id: 2, name: "Dummy3", category: "Test", price: 4.25 }
    ];
  };

  // Deletes a product.  There's a delete button in each row that triggers this.
  $scope.deleteProduct = function (product) {
    $scope.products.splice($scope.products.indexOf(product), 1);
  };

  // Adds a new product to the product list.
  $scope.createProduct = function (product) {
    $scope.products.push(product);
    $scope.displayMode = "list";
  };

  // Replaces an existing product by id.
  $scope.updateProduct = function (product) {
    for (var i = 0; i < $scope.products.length; i++) {
      if ($scope.products[i].id == product.id) {
        $scope.products[i] = product;
        break;
      }
    }
    $scope.displayMode = "list";
  };

  // Creates a new product or edits an existing product.
  // Uses a copy of the product when editing existing so cancel works.
  // Switches the UI to edit view.
  $scope.editOrCreateProduct = function (product) {
    $scope.currentProduct =
      product ? angular.copy(product) : {};
    $scope.displayMode = "edit";
  };

  // Saves new/edit product to products list.
  $scope.saveEdit = function (product) {
    if (angular.isDefined(product.id)) {
      $scope.updateProduct(product);
    } else {
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



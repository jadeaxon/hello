// Use an immediately invoked function expression to get rid of global variables.
(function () {

var module = angular.module('diveSiteApp', []);
module.controller('siteEditCtrl', SiteEditCtrl);

// Constructs a SiteEditCtrl.
function SiteEditCtrl($scope) {
  // Instead of using anonymous functions, you can do this.
  // Interesting that you can assign these all first before the functions are defined.
  $scope.sites = sites; // This is defined in sites.js.  It is the only global variable.
  $scope.startAdd = startAdd;
  $scope.cancel = cancel;
  $scope.add = add;
  $scope.startEdit = startEdit;
  $scope.save = save;
  $scope.startRemove = startRemove;
  $scope.remove = remove;
  $scope.getSelected = getSelected;

  var selected = -1; // Index of selected dive.  Nothing is selected initially.
  setView('list'); // Start out on the list view.

  // Sets the active view: list, add, edit, or delete.
  // ng-show directives cause only the active view to be shown.
  function setView(view) {
    $scope.view = view;
  }

  // Transitions to the add view.
  function startAdd() {
    $scope.siteBox = '';
    setView('add');
  }

  // Transitions to the list view by cancelling an add/edit/delete.
  function cancel() {
    setView('list');
  }

  // Adds a new dive site to the model (at least in the scope).
  // Transition to the list view.
  function add() {
    $scope.sites.push($scope.siteBox);
    setView('list');
  }

  // Transitions to the edit view (from the list view).
  // By passing in $index within ng-repeat, we know which dive site we're editing.
  function startEdit(index) {
    selected = index;
    $scope.siteBox = $scope.sites[index];
    setView('edit');
  }

  // On the edit view, saves the edit and transition back to the list view.
  function save() {
    $scope.sites[selected] = $scope.siteBox;
    setView('list');
  }

  // From the list view, transitions to the delete view.
  function startRemove(index) {
    selected = index;
    setView('delete');
  }

  // In the delete view, deletes dive from model and transition back to list view.
  function remove() {
    $scope.sites.splice(selected, 1);
    setView('list');
  }

  // Returns the currently selected dive site.
  // Pressing the edit or delete buttons causes a dive to be selecetd.
  function getSelected() {
    return sites[selected];
  }
}

})();


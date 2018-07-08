angular.module('maintenance', [])
  .controller('siteEditCtrl', SiteEditCtrl);

function SiteEditCtrl($scope) {
  $scope.sites = sites;
  $scope.startAdd = startAdd;
  $scope.cancel = cancel;
  $scope.add = add;
  $scope.startEdit = startEdit;
  $scope.save = save;
  $scope.startRemove = startRemove;
  $scope.remove = remove;
  $scope.getSelected = getSelected;

  var selected = -1;
  setView('list');

  function setView(view) {
    $scope.view = view;
  }

  function startAdd() {
    $scope.siteBox = '';
    setView('add');
  }

  function cancel() {
    setView('list');
  }

  function add() {
    $scope.sites.push($scope.siteBox);
    setView('list');
  }

  function startEdit(index) {
    selected = index;
    $scope.siteBox = $scope.sites[index];
    setView('edit');
  }

  function save() {
    $scope.sites[selected] = $scope.siteBox;
    setView('list');
  }

  function startRemove(index) {
    selected = index;
    setView('delete');
  }

  function remove() {
    $scope.sites.splice(selected, 1);
    setView('list');
  }

  function getSelected() {
    return sites[selected];
  }
}


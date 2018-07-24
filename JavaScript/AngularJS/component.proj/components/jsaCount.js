var module = angular.module('componentApp');
module.component('jsaCount', {
  templateUrl: 'components/jsaCount.html',
  controllerAs: 'component',
  controller: function($attrs) {
    this.min = $attrs['min'];
    this.max = $attrs['max'];
    this.numbers = [];
    for (var i = this.min; i <= this.max; i++) {
      this.numbers.push(i);
    }
  }
});



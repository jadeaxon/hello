angular.module('events', [])
.controller('dragCtrl', function ($scope) {
  var startX = 0, startY = 0,
    x = 0, y = 0;
  var element;
  var doc;

  $scope.mouseDown = mouseDown;

  function mouseDown(e) {
    element = angular.element('#item');
    doc = angular.element(document);
    e.preventDefault();
    startX = e.screenX - x;
    startY = e.screenY - y;
    doc.on('mousemove', mouseMove);
    doc.on('mouseup', mouseUp);
  }

  function mouseMove(e) {
    y = e.screenY - startY;
    x = e.screenX - startX;
    element.css({
      top: y + 'px',
      left: x + 'px'
    });
  }

  function mouseUp(e) {
    doc.off('mousemove', mouseMove);
    doc.off('mouseup', mouseUp);
  }
});

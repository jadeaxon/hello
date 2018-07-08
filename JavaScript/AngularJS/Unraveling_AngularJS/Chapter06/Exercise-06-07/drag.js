angular.module('events', [])
.directive('ywDraggable', function () {
  return function (scope, element, attr) {
    var startX = 0, startY = 0,
      x = 0, y = 0;
    var doc;

    element.css({
      'background-color': 'lightblue',
      'border': '2px solid navy',
      'padding': '8px',
      'text-align': 'center',
      'width': '160px',
      'position': 'relative',
      'display': 'block',
      'cursor': 'pointer'
    });
    element.on('mousedown', function (e) {
      doc = angular.element(document);
      e.preventDefault();
      startX = e.screenX - x;
      startY = e.screenY - y;
      doc.on('mousemove', mouseMove);
      doc.on('mouseup', mouseUp);
    });

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
  }
});

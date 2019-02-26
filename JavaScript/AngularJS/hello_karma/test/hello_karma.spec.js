// How do we access MainCtrl $scope?
describe('test hello_karma app', function() {
    it('main controller scope message is correct', function() {
        var message = 'Hello, Karma!';
        expect(message).toEqual('Hello, Karma!');
    });
});

describe('always win', function () {
    it('this should win', function() {
        expect(0).toEqual(0);
    })
});

// Try to use the app module and inject scope and controller into test.
describe('hello karma app', function() {
    // Before each test, initialize the app module (so that the controllers exist).
    // You need to aim at it in the files section of karma.conf.js.
    beforeEach(module('karma.app'));

    describe('MainCtrl', function(){
        var $scope, $controller;

        // Before each test, inject a scope and controller.
        // Use _ syntax to allow us to use $scope in the individual tests.
        beforeEach(inject(function(_$rootScope_, _$controller_) {
            $scope = _$rootScope_.$new();
            $controller = _$controller_('MainCtrl', {$scope: $scope});
        }));

        it('should initialize scope message', function() {
            expect($scope.message).toEqual("Hello, Karma!");
        });
    });
});

// Test a custom directive.
describe('<jsa-title>', function () {
  var $compile, $rootScope, $scope;

  // This makes our controllers available.
  beforeEach(module('karma.app'));

  beforeEach(inject(function (_$compile_, _$rootScope_, _$controller_) {
    $compile = _$compile_;
    $scope = _$rootScope_.$new();
    // Might be able to just do $scope = {} here and not use $rootScope at all.
    // <jsa-title> uses $scope.message, so we need to construct a MainCtrl controller to initialize that.
    $controller = _$controller_('MainCtrl', {$scope: $scope});
  }));

  it('<jsa-title> works in MainCtrl', function () {
    // Compile a piece of HTML containing the directive in the context of a MainCtrl $scope.
    var element = $compile("<jsa-title></jsa-title>")($scope);
    // This updates all the data bindings.
    // Apparently, when an element is compiled, it just sets up the watches/bindings but does not execute them.
    // So, to actually get {{message}} to use $scope.message, we need to call $scope.$digest().
    // If you comment out the line below, the test will fail.
    $scope.$digest();
    expect(element.html()).toContain("Hello, Karma!");
  });
});

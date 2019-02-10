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
        var scope, ctrl;

        // Before each test, inject a scope and controller.
        beforeEach(inject(function($rootScope, $controller) {
            scope = $rootScope.$new();
            ctrl = $controller('MainCtrl', {$scope: scope});
        }));

        it('should initialize scope message', function() {
            expect(scope.message).toEqual("Hello, Karma!");
        });
    });
});

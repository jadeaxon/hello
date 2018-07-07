// This file contains all the services for this app.
// I'm going to use the convention of prefixing custom services with $$.

//=============================================================================
// Classes
//=============================================================================

// Logger base class (constructor).
var baseLogger = function () {
  this.messageCount = 0;
  this.log = function (msg) {
    console.log(this.msgType + ": " + (this.messageCount++) + " " + msg);
  }
};

// Debug logger subclass using prototype-based inheritance.
var debugLogger = function () { };
debugLogger.prototype = new baseLogger();
debugLogger.prototype.msgType = "Debug";


// Error logger subclass using prototype-based inheritance.
var errorLogger = function () { };
errorLogger.prototype = new baseLogger();
errorLogger.prototype.msgType = "Error";


//=============================================================================
// Module
//=============================================================================

var module = angular.module("customServices", []);
module.factory("$$log", function () {
  // This object is only created once (it is a singleton).
  // Every consumer of the log service gets the same instance.

  // Including this variable by closure makes it not visible to service users.
  var messageCount = 0;
  var serviceSingleton = {
    log: function (msg) {
      console.log("(LOG + " + messageCount++ + ") " + msg);
    }
  };
  return serviceSingleton; // This will be accessible as $$log elsewhere.
});
module.service("$$debug", debugLogger)
module.service("$$error", errorLogger);

// A (service) provider also returns a service but more indirectly.
// The $get function is called.  This can be used to configure the service.
// For example, you might want a dev/test/production database connection.
// For DI, $$plog is the service name while $$plogProvider is the service provider name.
// module.config(function ($$plogProvider) {}) is used to configure the service provider.
module.provider("$$plog", function() {
  // These act as private instance vars of the provider via closure.
	var counter = true;
	var debug = true;

  // The provider object is used to configure the service.
  // Its $get() method returns the actual service object.
  var provider = {
    // These config methods are chainable.
    // If you pass in a value, they return the provider.
    // If you pass in nothing, they return the config value.
		messageCounterEnabled: function (setting) {
			if (angular.isDefined(setting)) {
				counter = setting;
				return this;
			}
      else {
				return counter;
			}
		},
		debugEnabled: function(setting) {
			if (angular.isDefined(setting)) {
				debug = setting;
				return this;
			}
      else {
				return debug;
			}
		},
    // $get() returns the actual service singleton.
    $get: function () {
      var serviceSingleton = {
        messageCount: 0,
        log: function (msg) {
          if (debug) {
            console.log("(DEBUG_PLOG" + (counter ? " + " + this.messageCount++ + ") " : ") ") + msg);
          }
          else {
            console.log("(PLOG + " + this.messageCount++ + ") " + msg);
          }
        } // log()
      }; // serviceSingleton
      return serviceSingleton;
    } // $get()
  }; // provider
  return provider;
});

// Configure the service via the provider.
// What you are passing config is a function that configures the service provider.
// The provider is injected into this configurator by adding Provider suffix to service name.
module.config(function ($$plogProvider) {
  $$plogProvider.debugEnabled(true).messageCounterEnabled(false);
  // Now you can use the configured $$plog service anywhere in your app.
});




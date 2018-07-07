// This file contains all the services for this app.
// I'm going to use the convention of prefixing custom services with $$.

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



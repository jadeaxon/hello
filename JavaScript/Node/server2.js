#!/usr/bin/env node

// Import the core HTTP networking module.
var http = require("http");

// Create an HTTP server.
var server = http.createServer(
	// This is the request handler function.
	function(request, response) {
		console.log("Request received.");

		response.write("Hello, HTTP client!");
		response.end();
	}
);

// Listen for requests on TCP port 3000.
var port = 3000;
server.listen(port);
console.log("Server listening for requests at http://localhost:" + port + ".");



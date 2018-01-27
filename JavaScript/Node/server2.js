#!/usr/bin/env node

// Import the core HTTP networking module.
var http = require("http");

// Handles an HTTP request.
function requestHandler(request, response) {
	console.log("Request received.");
	console.log("Request headers:");
	console.log(request.headers);

	response.write("Hello, HTTP client!");
	response.end();
}

// Create an HTTP server.
var server = http.createServer(requestHandler);

// Listen for requests on TCP port 3000.
var port = 3000;
server.listen(port);
console.log("Server listening for requests at http://localhost:" + port + ".");



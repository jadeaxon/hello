#!/usr/bin/env node

// Import the core HTTP networking module.
var http = require("http");

var log = console.log;

// Handles an HTTP request.
function requestHandler(request, response) {
	var client = "HTTP client";

	log("Request received.");
	log("Request method: " + request.method); // The HTTP method.
	log("Request URL: " + request.url);
	log("Request headers:");
	log(request.headers); // request.headers is a map object.
	var userAgent = request.headers["user-agent"];
	log("user-agent: " + userAgent);
	if (userAgent.indexOf("curl") !== -1) {
		client = "curl";
	}

	// Once you do the first write() you can no longer change response headers.
	response.setHeader("content-type", "text/plain"); // MIME type.
	response.write("Hello, " + client + "!");
	response.end();
}

// Create an HTTP server.
var server = http.createServer(requestHandler);

// Listen for requests on TCP port 3000.
var port = 3000;
server.listen(port);
log("Server listening for requests at http://localhost:" + port + ".");



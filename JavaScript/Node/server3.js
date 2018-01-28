#!/usr/bin/env node

var http = require("http");
var fs = require("fs");
var log = console.log;

// Generates an HTTP 404 response (resource not found).
function send404(response) {
	response.writeHead(404, {'content-type': 'text/plain'});
	response.write('Error 404: Resource not found.');
	response.end();
}

// Handles incoming HTTP GET requests.
function requestHandler(request, response) {
	if (request.method === "GET") {
		if (request.url === "/") {
			response.writeHead(
				200,
				{'content-type': 'text/html'}
			);
			fs.createReadStream("html/index.html").pipe(response);
		}
		else { // index.html DNE
			send404(response);
		}
	}
}

var server = http.createServer(requestHandler);
var port = 3000;
server.listen(port);
log("Server listening for requests at http://localhost:" + port + ".");



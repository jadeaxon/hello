#!/usr/bin/env node

// This web server can serve up anything in the html/ subdir
// of the directory where it is launched.

var http = require("http");
var fs = require("fs");
var path = require("path");
var mime = require("mime");

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
		var url = request.url; // Local URL.
		if (url === "/") url = "/index.html";
		var filepath = path.resolve("./html" + url);
		var ext = path.extname(filepath);

		var mimeType = mime.getType(ext);
		if (!mimeType) {
			send404(response);
			return;
		}

		// Does this run async?
		fs.exists(
			filepath,
			// What to do if the given path exists or not.
			function (exists) {
				if (!exists) {
					// Hmmm, this does know about response.
					// So, it is an anonymous closure.
					send404(response);
					return;
				}
				response.writeHead(
					200,
					{'content-type': mimeType}
				);
				fs.createReadStream(filepath).pipe(response);
			} // function (exists)
		); // fs.exists
	}
	else { // Not a GET request.
		send404(response);
	}
} // requestHandler()

var server = http.createServer(requestHandler);
var port = 3000;
server.listen(port);
log("Server listening for requests at http://localhost:" + port + ".");



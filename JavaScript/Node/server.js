#!/usr/bin/env node

// A static file server using Node.js.
// PRE: Node.js has been installed.
// Run this using the following:
// node server.js

// Import a bunch of libraries.
// var sys = require("sys"); // Deprecated.
var util = require("util");
var http = require("http");
var url = require("url");
var path = require("path");
var fs = require("fs"); // Filesystem

var port = 8181; // The TCP port to listen on.

console.log("Creating HTTP server.");

// An HTTP server gives responses to requests.
var server = http.createServer(
	function(request, response) {
		console.log("Request: " + request.url);
		// Parse the path out of the URL.
		var uri = url.parse(request.url).pathname;
		// Interpret the paths as relative to where this server process is running.
		var filename = path.join(process.cwd(), uri);
		// Check if the desired file exists.
		fs.exists(filename,
			function(exists) {
				if (!exists) {
					response.writeHead(
						404,
						{ "Content-Type": "text/plain" }
					);
					response.end("404 Not Found\n");
					return;
				}
				// If the file exists, respond with it as binary output.
				fs.readFile(
					filename,
					"binary",
					function(err, file) {
						if (err) {
							response.writeHead(
								500,
								{ "Content-Type": "text/plain" }
							);
							response.end(err + "\n");
							return;
						}
						response.writeHead(200);
						response.end(file, "binary");
					}
				);
			}
		); // file exists
	}
);
server.listen(port);
console.log("Server running at http://localhost:" + port + "/");



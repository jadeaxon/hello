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
var fs = require("fs");

http.createServer(
	function(request, response) {
		var uri = url.parse(request.url).pathname;
		var filename = path.join(process.cwd(), uri);
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
).listen(8080);
console.log("Server running at http://localhost:8080/");



#!/usr/bin/env node

// This server does everything server3.js does in far less lines of code.

var log = console.log;
var express = require('express');
var serveIndex = require('serve-index');
var app = express();
// __dirname is the current working dir of this process.
// serveStatic is a Connect/Express middleware for serving static web pages.
var docroot = __dirname + '/html';
app.use(express.static(docroot));
app.use(serveIndex(docroot)); // Display list of files in a directory.
app.listen(3000);
log("Listening for HTTP requests on port 3000.");



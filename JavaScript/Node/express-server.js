#!/usr/bin/env node

// This server does everything server3.js does in far less lines of code.

var log = console.log;
var express = require('express');
var app = express();
// __dirname is the current working dir of this process.
// serveStatic is a Connect/Express middleware for serving static web pages.
app.use(express.static(__dirname + '/html'))
app.listen(3000);
log("Listening for HTTP requests on port 3000.");



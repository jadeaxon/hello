// PRE: npm install express
// Run web server: node webserver.py
// Connect to web server: http://localhost:5000/

var express = require('express');
var serveStatic = require('serve-static');
 
var app = express();

// Serve static HTML files from the html/ subdir.
app.use(serveStatic('html', {'index': ['index.html', 'index.htm']}));
app.listen(5000);



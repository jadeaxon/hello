var fs = require('fs');
var http = require('http').createServer(
    function(req, res) {
        fs.readFile("main.html", function (err, data) {
            if (err) {
                res.writeHead(404);
                res.end('Not found' + err);
            }
            res.end(data);
        });
    }
).listen(1234, '127.0.0.1');

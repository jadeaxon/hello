var connect = require('connect');
var serveStatic = require('serve-static');

var app = connect();
app.use(serveStatic("../Work/UnravelNg"));
app.listen(5100);

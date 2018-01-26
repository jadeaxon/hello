#!/usr/bin/env node
// Yup, the shebang line works for Node.js.

// List all the command-line args.
// argv[0] == the node interpreter path
// argv[1] == the path to this script
// argv[2] == the first command-line argument
for (var i = 0; i < process.argv.length; i++) {
	console.log("process.argv[" + i + "] = " + process.argv[i]);
} // next command-line arg



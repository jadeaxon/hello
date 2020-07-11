composer.json
	Config file for Composer PHP package/dependency manager.


	PRE: Use Cygwin installer to install php-json, php-phar, php-iconv, and php-zlib.
	To install Composer, see https://getcomposer.org/download/.

instructions.txt
	Instructions for running this web app.

app/
	Application files.
	Based on the application framework in system/.

	Config.php
	Controllers/
	Models/
	views/

system/
	Core framework files.
	This is the book's basic application framework.

	BaseController.php
	BaseModel.php
	Route.php
	View.php

vendor/
	3rd-party packages downloaded by Composer.
	Should be ignored by Git.

webroot/
	Publicly available files.

	.htaccess
		URL rewrite rules.

	index.php
		Main page of the app.



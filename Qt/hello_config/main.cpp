// C++
#include <iostream>

// Qt
// All of Qt's header files, classes, etc. start with Q.
#include <QApplication>

// hello_config
#include "Configuration.h"


// In Cygwin:
// qmake -project # If no .pro file yet.
// qmake
// make
// ./hello_config.exe

using namespace std;


// Like any other C++ program, a Qt program starts in main.
int main(int argc, char* argv[]) {
	// Create an application.
	QCoreApplication app(argc, argv);

	cout << "Loading configuration." << endl;
	Configuration config("digeplayer.conf");
	config.print();
	
	// Start the main event loop for the application.
	// Now, you have an event-driven GUI.
	return app.exec();
} // main(...)




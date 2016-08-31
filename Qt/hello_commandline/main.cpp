// Qt
// All of Qt's header files, classes, etc. start with Q.
// Qt's library header files all start with Qt.
// Using them keeps you from having to include headers for every single class.
// The QtCore and QtGui libraries are linked into every Qt app by default.
// Since
#include <QtCore>

// In Cygwin:
// qmake -project # If no .pro file yet.
// qmake
// make
// ./hello_commandline.exe


// Like any other C++ program, a Qt program starts in main.
int main(int argc, char* argv[]) {
	// Create a non-GUI application.
	QCoreApplication app(argc, argv);
	
	
	// Create a GUI.
	QString hi("Hello, world!");
	qDebug() << hi;

	// Start the main event loop for the application.
	// A non-GUI app can still use signals/slots.  So you can use things like timers and threads.
	return app.exec();
}



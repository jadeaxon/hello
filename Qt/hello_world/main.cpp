// Qt
// All of Qt's header files, classes, etc. start with Q.
#include <QApplication>
#include <QLabel>

// In Cygwin:
// qmake -project # If no .pro file yet.
// qmake
// make
// startx & # If you haven't already started Cygwin's X Windows server.
// export DISPLAY=:1.0
// ./hello_world.exe


// Like any other C++ program, a Qt program starts in main.
int main(int argc, char* argv[]) {
	// Create an application.
	QApplication app(argc, argv);
	
	
	// Create a GUI.
	QLabel label("Hello, world!");
	label.show();

	// Start the main event loop for the application.
	// Now, you have an event-driven GUI.
	return app.exec();
}



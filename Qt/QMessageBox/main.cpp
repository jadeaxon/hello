// Qt
// All of Qt's header files, classes, etc. start with Q.
#include <QApplication>
#include <QLabel>
#include <QMessageBox>
#include <QString>
#include <QObject> // For tr().

// C++ Standard Library
#include <iostream>

using namespace std;

bool askQuestion(const QString&);

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


	// This actually works because the dialog starts its own event loop.
	bool answer = askQuestion("blahblahblah");
	cout << answer << endl;

	// Start the main event loop for the application.
	// Now, you have an event-driven GUI.
	return app.exec();

} // main(...)



// Asks the user a question via a modal dialog box.
bool askQuestion(const QString& filename) {
	int status = QMessageBox::question(
			NULL,
			QObject::tr("Overwrite File?"),
			QObject::tr("A file called ’%1’ already exists. \n"
			   "Do you realy want to overwrite this file?")
			.arg(filename),
			QMessageBox::Yes|QMessageBox::Default,
			QMessageBox::No|QMessageBox::Escape,
			QMessageBox::NoButton
	);
	if (status != QMessageBox::Yes) return false;
	return true;

} // askQuestion()




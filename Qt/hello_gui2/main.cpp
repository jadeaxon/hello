#include <QApplication>
#include <QLabel>

// Qt essentially makes C++ work more like Java.

// To get this to work in Cygwin X Windows:
// DISPLAY=:1.0
// startx &
// qmake
// make
// ./hello_gui2

// Displays a label in a window.
int main(int argc, char* argv[]) {
	// The application can serve as the parent of all dynamically allocated objects.
	// This ensures they will be properly cleaned up when app exits.
	//
	// Qt supports certain commandline options (like -qws).
	// So, first you let Qt extract the commandline options it is interested in.
	// Then, you parse whatever is left.
	QApplication app(argc, argv);


	// GUIs are composed of widgets.
	// If you show a widget, Qt will automatically wrap it in a window.
	// widget => window gadget (a component used in a window, like a button).
	// Qt has a variety of built-in widgets (like Swing).
	QLabel* label = new QLabel("Hello, Qt!");
	
	// Most Qt widgets can render HTML.
	QLabel* label2 = new QLabel(
		"<h2><i>Hello, </i>" // In C++, adjacent strings concatenate.
		"<font color=red>Qt!</font></h2>"
	);
	label2->show();
	
	// This starts the main event loop of the app.
	// The app has just one event loop.  All events are routed through here.
	return app.exec();

} // main(...)



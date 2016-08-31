#include <QApplication>
#include <QPushButton>

// Displays a button which you can press to quit the app.
int main(int argc, char* argv[]) {
	// Create application and delegate commandline arg processing.
	QApplication app(argc, argv);
	
	// Create a push button widget.
	QPushButton* button = new QPushButton("Quit");
	
	// connect() is a static method of QObject that creates reaction links (connections)
	// between objects.
	//
	// Reaction wiring.
	// When the button emits a clicked signal/event, the app should invoke its quit method.
	//
	// The args are QObject pointers.
	// Note the use of the SIGNAL and SLOT macros (defined by Qt).
	QObject::connect(
		button, SIGNAL(clicked()),
		&app, SLOT(quit())
	);
	

	// Show the button (implicitly wrapping it in a window).
	button->show();

	// Start handling events.
	return app.exec();

} // main(...)



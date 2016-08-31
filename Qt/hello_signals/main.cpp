#include <QApplication>
#include <QPushButton>


// An app that just has a quit button.  Demonstrates hooking a signal to a slot.
int main(int argc, char* argv[]) {
	QApplication a(argc, argv);
	QPushButton button("Quit");
	button.show();

	// When a button is clicked, it emits a clicked() signal.
	// We connect that signal to the quit() slot of the application.
	// A slot is just a method that can be triggered by a signal.
	QObject::connect(
		&button, SIGNAL(clicked()),
		&a, SLOT(quit())
	);

	// Starts the event loop.  This will allow the button to know it has been clicked
	// by the user.  In turn, the button will emit a signal which we have no connected
	// to a slot method of the application object.  So, we wire up a chain reaction of
	// things to happen based on user interaction via the mouse, keyboard, etc.
	
	// You can also use timers to periodically emit signal instead of relying on the user
	// to do something all the time.
	return a.exec();
}

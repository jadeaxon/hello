#include <QApplication>

#include "FindDialog.h"


int main(int argc, char* argv[]) {
	QApplication app(argc, argv); // Delegate commandline args.
	FindDialog* dialog = new FindDialog(); // Create widget.
	dialog->show(); // Show it (implicit window added).
	return app.exec(); // Start main event loop.

}



#include "ThreadDialog.h"

// Qt
#include <QApplication>


// Displays a dialog which lets you launch one of two worker threads.
int main(int argc, char* argv[]) {
    // There must be exactly one QApplication object in a Qt GUI application.
    QApplication app(argc, argv);

    // Create GUI components (widgets).
    ThreadDialog dialog;


    // Show the GUI component.  Looks like there isn't a main window class like Java JFrame.
    // Well, what happens is that Qt is smart enough to wrap the widget in a window if it realizes it is not contained
    // by one already.
    dialog.show();

    // This starts the actual event loop (which is part of QApplication).  Otherwise the GUI would do nothing.
    return app.exec();

} // main(...)


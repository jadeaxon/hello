// Qt
#include <QApplication>

// cuteedit2
#include "MainWindow.h"


// A simple text editor with some sort of template ability.
int main(int argc, char* argv[]) {
    QApplication a(argc, argv);

    QCoreApplication::setOrganizationName("OpenSourcePress");
    QCoreApplication::setOrganizationDomain("OpenSourcePress.de");
    QCoreApplication::setApplicationName("CuteEdit");
    
	MainWindow mainWindow;
    mainWindow.show();

    return a.exec();
} // main(...)



// Qt
#include <QApplication>
// #include <QMainWindow>
#include <QLabel>

// hello_mainwindow
#include "MainWindow.h"


int main(int argc, char* argv[]) {
	QApplication a(argc, argv);

	QLabel* label = new QLabel("<center>Central Widget</center>");
	
	// QMainWindow mainWindow;
	// Generally, you use a custom subclass of QMainWindow for your app.
	MainWindow mainWindow;
	
	mainWindow.setCentralWidget(label);
	mainWindow.show();

	return a.exec();

} // main(...)



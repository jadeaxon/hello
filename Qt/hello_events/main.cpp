#include <QtGui>
#include <QTextEdit>
#include <QObject>

#include <EventWidget.h>


int main(int argc, char** argv) {
	QApplication app(argc, argv);
	QTextEdit log;
	EventWidget widget;
	QObject::connect(
		&widget, SIGNAL(gotEvent(const QString&)), 
		&log, SLOT(append(const QString&))
	);

	// Hmmm... How is it showing both widgets?
	log.show();
	widget.show();
	return app.exec();
}




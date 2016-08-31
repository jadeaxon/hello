// Qt
#include <QApplication>

#include "UnixSocketClient.h"
#include "UnixSocketServer.h"
#include "UnixSocketWindow.h"


// Exercises the socket-related classes.
int main(int argc, char** argv) {
	QApplication app(argc, argv);

	UnixSocketClient client;
	client.start();
	::sleep(10);
	client.stop();
	client.wait();

	return 0;

} // main(...)


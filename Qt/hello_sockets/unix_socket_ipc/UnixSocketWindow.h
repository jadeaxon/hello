#pragma once

// Qt
#include <QWidget>


// IPC
#include <UnixSocketServer.h>
#include <UnixSocketClient.h>


// A window which displays interaction between a Unix socket client and server.
class UnixSocketWindow : QWidget {
	Q_OBJECT

	private:
		UnixSocketServer* server;
		UnixSocketClient* client;


}; // class



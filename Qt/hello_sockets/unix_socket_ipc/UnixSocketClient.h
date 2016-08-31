#pragma once

#include <QThread>

// #include <QLocalSocket> // Unix socket client (on Windows uses named pipes).
#include <QLocalSocket>


// A worker thread that writes to a Unix socket.
// That is, this is a client thread.  What it writes is a request to a Unix socket server.
// So, this would be the thread running in the Glide daemon that makes a request to a
// server thread in a digEplayer application to do something.
// 
// That socket server thread would then send a Qt signal to the main thread (UI thread).  The Device
// instance in the main thread would then route the QString message to a method.  That method would
// then cause whatever is supposed to happen to happen.
//
// That is, each digEplayer application has a Unix socket server thread used for IPC with the Glide daemon.
class UnixSocketClient : public QThread {
	Q_OBJECT	

	public:
		UnixSocketClient();
		~UnixSocketClient();
		
		
		// Requests this thread to stop gracefully.
		void stop();

		// This class has no signals/slots.
		// It would run in the Glide daemon.
		// It just does IPC as a Unix socket client to various Unix socket servers.
		// Each major digEplayer app is a Unix socket server.


	protected:
		// Override.
		void run(); 
			 

	private:	
	
		// Whether this thread has been requested to stop by another thread.
		volatile bool stopped;


		// Qt object that represents a Unix socket (under Linux at least).
		QLocalSocket* socket;


}; // class UnixSocketClient





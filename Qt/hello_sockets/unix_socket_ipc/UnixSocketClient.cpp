#include "UnixSocketClient.h"


//==============================================================================
// Constructor, Initializers, Destructor
//==============================================================================


UnixSocketClient::UnixSocketClient() : QThread() {
	// TO DO: Open socket.

}

UnixSocketClient::~UnixSocketClient() {

}


//==============================================================================
// Thread 
//==============================================================================


// Runs this code in its own thread.  Basically just prints a message over and over again.
void UnixSocketClient::run() {
	static int count = 0; // Are static vars thread-local?  Probably not. . . .

	forever {
		if (this->stopped) break;

		count++;
		// TO DO: Send this message over socket.
		qDebug() << "UnixSocketClient: Message " << count << ".";
		QThread::sleep(1);

	} // next message

	// TO DO: Any necessary cleanup?


} // run()


// Requests that this thread stop gracefully.
void UnixSocketClient::stop() {
	this->stopped = true;

}




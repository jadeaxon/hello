#include <Thread.h>

// Standard library
#include <iostream>


// Creates worker thread.  Starts out not running.
Thread::Thread() : QThread() {
	stopped = false;
}


// This is what executes in its own system thread.
// The run() function is called to start executing the thread. As long as the stopped variable is false, the function keeps
// printing the given message to the console. The thread terminates when control leaves the run() function.
// Basically, we are just printing a message over and over again.
// We set stopped to false in the constructor.
void Thread::run() {
	// It is typical to use this kind of flag to stop a thread gracefully.
	while (!stopped) {
		std::cerr << qPrintable(message);
	}
	stopped = false;
	std::cerr << std::endl;
}


// Stops this thread.
void Thread::stop() {
	stopped = true;
}


// Sets the message to print out while this thread is running.
void Thread::setMessage(const QString& message) {
	this->message = message;
}


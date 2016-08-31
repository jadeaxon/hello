#pragma once

#include <QThread>

class UnixSocketServer : QThread {
	Q_OBJECT

	private:
		int crap;


	protected:
		void run();

	public:
		UnixSocketServer();
		~UnixSocketServer();


}; // class

